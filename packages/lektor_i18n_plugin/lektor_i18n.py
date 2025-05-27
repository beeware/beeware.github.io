# -*- coding: utf-8 -*-
#pylint: disable=wrong-import-position
import sys

PY3 = sys.version_info > (3,)

import collections
import datetime
import gettext
import os
from os.path import relpath, join, exists, dirname
from pprint import PrettyPrinter
import re
import tempfile
import time
if PY3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

from lektor.pluginsystem import Plugin
from lektor.db import Page
from lektor.metaformat import tokenize
from lektor.reporter import reporter
from lektor.types.flow import FlowType, process_flowblock_data
from lektor.utils import portable_popen, locate_executable
from lektor.environment import PRIMARY_ALT
from lektor.filecontents import FileContents
from lektor.context import get_ctx



command_re = re.compile(r'([a-zA-Z0-9.-_]+):\s*(.*?)?\s*$')
# derived from lektor.types.flow but allows more dash signs
block2re = re.compile(r'^###(#+)\s*([^#]*?)\s*###(#+)\s*$')

POT_HEADER = """msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: %(NOW)s\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: %(LANGUAGE)s <LL@li.org>\\n"
"Language: %(LANGUAGE)s\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"

"""


# python2/3 compatibility layer

encode = lambda s: (s if PY3 else s.encode('UTF-8'))

def trans(translator, s):
    """Thin gettext translation wrapper to allow compatibility with both Python2
    and 3."""
    if PY3:
        return translator.gettext(s)
    else:
        return translator.ugettext(s)


def truncate(s, length=32):
    return (s[:length] + '..') if len(s) > length else s

#pylint: disable=too-few-public-methods,redefined-variable-type
class TemplateTranslator(object):
    def __init__(self, i18npath):
        self.i18npath = i18npath
        self.__lastlang = None
        self.translator = None
        self.init_translator()

    def init_translator(self):
        ctx = get_ctx()
        if not ctx:
            self.translator = gettext.GNUTranslations()
            return super(TemplateTranslator, self).__init__()
        if not self.__lastlang == ctx.locale:
            self.__lastlang = ctx.locale
            self.translator = gettext.translation("contents",
                    join(self.i18npath, '_compiled'),
                    languages=[ctx.locale], fallback=True)

    def gettext(self, x):
        self.init_translator() # lagnuage could have changed
        return self.translator.gettext(x)

    def ngettext(self, *x):
        self.init_translator()
        return self.translator.ngettext(*x)


class Translations():
    """Memory of translations"""

    def __init__(self):
        # dict like {'text' : ['source1', 'source2',...],}
        self.translations = collections.OrderedDict()

    def add(self, text, source):
        if not text in self.translations.keys():
            self.translations[text]=[]
            reporter.report_debug_info('added to translation memory : ', truncate(text))
        if not source in self.translations[text]:
            self.translations[text].append(source)

    def __repr__(self):
        return PrettyPrinter(2).pformat(self.translations)

    def as_pot(self, content_language):
        """returns a POT version of the translation dictionary"""
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        now += '+%s'%(time.tzname[0])
        result = POT_HEADER % {'LANGUAGE': content_language, 'NOW': now}

        for msg, paths in self.translations.items():
            if msg:
                result += "#: %s\n" % " ".join(paths)
                for token, repl in {'\\': '\\\\', '\n': '\\n', '\t': '\\t', '"': '\\"'}.items():
                    msg = msg.replace(token, repl)
                result += 'msgid "%s"\n' % msg
                result += 'msgstr ""\n\n'
        return result

    def write_pot(self, pot_filename, language):
        if not os.path.exists(os.path.dirname(pot_filename)):
            os.makedirs(os.path.dirname(pot_filename))
        with open(pot_filename,'w') as f:
            f.write(encode(self.as_pot(language)))

    def merge_pot(self, from_filenames, to_filename):
        msgcat=locate_executable('msgcat')
        if msgcat is None:
            msgcat="/usr/bin/msgcat"
        cmdline=[msgcat, "--use-first"]
        cmdline.extend(from_filenames)
        cmdline.extend(("-o", to_filename))
        reporter.report_debug_info('msgcat cmd line', cmdline)
        portable_popen(cmdline).wait()

    def parse_templates(self, to_filename):
        pybabel=locate_executable('pybabel')
        if pybabel is None:
            pybabel="/usr/bin/pybabel"
        cmdline=[pybabel, 'extract', '-F', 'babel.cfg', "-o", to_filename, "./"]
        reporter.report_debug_info('pybabel cmd line', cmdline)
        portable_popen(cmdline).wait()

translations = Translations() # let's have a singleton

class POFile():

    FILENAME_PATTERN = "contents+%s.po"

    def __init__(self, language, i18npath):
        self.language=language
        self.i18npath=i18npath

    def _exists(self):
        """Returns True if <language>.po file exists in i18npath"""
        filename=self.FILENAME_PATTERN%self.language
        return exists( join(self.i18npath, filename) )

    def _msg_init(self):
        """Generates the first <language>.po file"""
        msginit=locate_executable('msginit')
        cmdline=[msginit, "-i", "contents.pot", "-l", self.language, "-o", self.FILENAME_PATTERN%self.language, "--no-translator"]
        reporter.report_debug_info('msginit cmd line', cmdline)
        portable_popen(cmdline, cwd=self.i18npath).wait()

    def _msg_merge(self):
        """Merges an existing <language>.po file with .pot file"""
        msgmerge=locate_executable('msgmerge')
        cmdline=[msgmerge, self.FILENAME_PATTERN%self.language, "contents.pot", "-U", "-N", "--backup=simple"]
        reporter.report_debug_info('msgmerge cmd line', cmdline)
        portable_popen(cmdline, cwd=self.i18npath).wait()

    def _prepare_locale_dir(self):
        """Prepares the i18n/<language>/LC_MESSAGES/ to store the .mo file ; returns the dirname"""
        directory = join('_compiled',self.language, "LC_MESSAGES")
        try:
            os.makedirs(join(self.i18npath, directory))
        except OSError:
            pass # already exists, no big deal
        return directory

    def _msg_fmt(self, locale_dirname):
        """Compile an existing <language>.po file into a .mo file"""
        msgfmt=locate_executable('msgfmt')
        cmdline=[msgfmt, self.FILENAME_PATTERN%self.language, "-o", join(locale_dirname,"contents.mo")]
        reporter.report_debug_info('msgfmt cmd line', cmdline)
        portable_popen(cmdline, cwd=self.i18npath).wait()

    def generate(self):
        if self._exists():
            self._msg_merge()
        else:
            self._msg_init()

    def compile(self):
        if self._exists():
            locale_dirname=self._prepare_locale_dir()
            self._msg_fmt(locale_dirname)

def line_starts_new_block(line, prev_line):
    """Detect a new block in a lektor document. Blocks are delimited by a line
    containing 3 or more dashes. This actually matches the definition of a
    markdown level 2 heading, so this function returns False if no colon was
    found in the line before, so if it isn't a new block with a key: value pair
    before."""
    if not prev_line or ':' not in prev_line:
        return False # could be a markdown heading
    line = line.strip()
    return line == u'-' * len(line) and len(line) >= 3




def split_paragraphs(document):
    if isinstance(document, (list, tuple)):
        document = ''.join(document) # list of lines
    return re.split('\n(?:\\s*\n){1,}', document)

# We cannot check for unused arguments here, they're mandated by the plugin API.
#pylint:disable=unused-argument
class I18NPlugin(Plugin):
    name = u'i18n'
    description = u'Internationalisation helper'

    def translate_tag(self, s, *args, **kwargs):
        if not self.enabled:
            return s # no operation
        s = s.strip()
        ctx = get_ctx()
        if self.content_language==ctx.locale:
            translations.add(s,'(dynamic)')
            reporter.report_debug_info('added to translation memory (dynamic): ', truncate(s))
            return s
        else:
            translator = gettext.translation("contents", join(self.i18npath,'_compiled'), languages=[ctx.locale], fallback = True)
            return trans(translator, s)

    def choose_language(self, l, language, fallback='en', attribute='language'):
        """Will return from list 'l' the element with attribute 'attribute' set to given 'language'.
        If none is found, will try to return element with attribute 'attribute' set to given 'fallback'.
        Else returns None."""
        language=language.strip().lower()
        fallback=fallback.strip().lower()
        for item in l:
            if item[attribute].strip().lower()==language:
                return item
        # fallback
        for item in l:
            if item[attribute].strip().lower()==fallback:
                return item
        return None

    #pylint: disable=attribute-defined-outside-init
    def on_setup_env(self, **extra):
        """Setup `env` for the plugin"""
        # Read configuration
        self.enabled = self.get_config().get('enable', 'true') in ('true','True','1')
        if not self.enabled:
            reporter.report_generic('I18N plugin disabled in configs/i18n.ini')

        self.i18npath = self.get_config().get('i18npath', 'i18n')
        self.url_prefix = self.get_config().get('url_prefix', 'http://localhost/')
        # whether or not to use a pargraph as smallest translatable unit
        self.trans_parwise = self.get_config().get('translate_paragraphwise',
                'false') in ('true','True','1')
        self.content_language=self.get_config().get('content', 'en')
        self.env.jinja_env.add_extension('jinja2.ext.i18n')
        self.env.jinja_env.policies['ext.i18n.trimmed'] = True # do a .strip()
        self.env.jinja_env.install_gettext_translations(TemplateTranslator(self.i18npath))
        # ToDo: is this still required
        try:
            self.translations_languages=self.get_config().get('translations').replace(' ','').split(',')
        except AttributeError:
            raise RuntimeError('Please specify the "translations" configuration option in configs/i18n.ini')

        if not self.content_language in self.translations_languages:
            self.translations_languages.append(self.content_language)

        self.env.jinja_env.filters['translate'] = self.translate_tag
        self.env.jinja_env.globals['_'] = self.translate_tag
        self.env.jinja_env.globals['choose_language'] = self.choose_language

    def process_node(self, fields, sections, source, zone, root_path):
        """For a given node (), identify all fields to translate, and add new
        fields to translations memory. Flow blocks are handled recursively."""
        for field in fields:
            if ('translate' in field.options) \
                    and (source.alt in (PRIMARY_ALT, self.content_language)) \
                    and (field.options['translate'] in ('True', 'true', '1', 1)):
                if field.name in sections.keys():
                    section = sections[field.name]
                    # if blockwise, each paragraph is one translatable message,
                    # otherwise each line
                    chunks = (split_paragraphs(section) if self.trans_parwise
                            else [x.strip() for x in section if x.strip()])
                    for chunk in chunks:
                        translations.add(chunk.strip('\r\n'),
                            "%s (%s:%s.%s)" % (
                                urljoin(self.url_prefix, source.url_path),
                                relpath(source.source_filename, root_path),
                                zone, field.name)
                            )

            if isinstance(field.type, FlowType):
                if field.name in sections:
                    section = sections[field.name]
                    for blockname, blockvalue in process_flowblock_data("".join(section)):
                        flowblockmodel = source.pad.db.flowblocks[blockname]
                        blockcontent=dict(tokenize(blockvalue))
                        self.process_node(flowblockmodel.fields, blockcontent, source, blockname, root_path)


    def __parse_source_structure(self, lines):
        """Parse structure of source file. In short, there are two types of
        chunks: those which need to be translated ('translatable') and those
        which don't ('raw'). "title: test" could be split into:
        [('raw': 'title: ',), ('translatable', 'test')]
        NOTE: There is no guarantee that multiple raw blocks couldn't occur and
        in fact due to implementation details, this actually happens."""
        blocks = []
        count_lines_block = 0 # counting the number of lines of the current block
        is_content = False
        prev_line = None
        for line in lines:
            stripped_line = line.strip()
            if not stripped_line: # empty line
                blocks.append(('raw', '\n'))
                continue
            # line like "---*" or a new block tag
            if line_starts_new_block(stripped_line, prev_line) or \
                    block2re.search(stripped_line):
                count_lines_block=0
                is_content = False
                blocks.append(('raw', line))
            else:
                count_lines_block+=1
                match = command_re.search(stripped_line)
                if count_lines_block==1 and not is_content and match: # handle first line, while not in content
                    key, value = match.groups()
                    blocks.append(('raw', encode(key) + ':'))
                    if value:
                        blocks.append(('raw', ' '))
                        blocks.append(('translatable', encode(value)))
                    blocks.append(('raw', '\n'))
                else:
                    is_content=True
            if is_content:
                blocks.append(('translatable', line))
            prev_line = line
        # join neighbour blocks of same type
        newblocks = []
        for type, data in blocks:
            if len(newblocks) > 0 and newblocks[-1][0] == type: # same type, merge
                newblocks[-1][1] += data
            else:
                newblocks.append([type, data])
        return newblocks


    def translate_contents(self):
        """Produce all content file alternatives (=translated pages)
        using the gettext translations available."""
        for root, _, files in os.walk(os.path.join(self.env.root_path, 'content')):
            if re.match('content$', root):
                continue
            if 'contents.lr' in files:
                fn = os.path.join(root, 'contents.lr')
                contents = FileContents(fn)
                for language in self.translations_languages:
                    translator = gettext.translation("contents", join(self.i18npath, '_compiled'), languages=[language], fallback=True)
                    translated_filename = os.path.join(root, "contents+%s.lr" % language)
                    with contents.open(encoding='utf-8') as file:
                        chunks = self.__parse_source_structure(file.readlines())
                    with open(translated_filename, "w") as f:
                        for type, content in chunks:  # see __parse_source_structure
                            if type == 'raw':
                                f.write(content)
                            elif type == 'translatable':
                                if self.trans_parwise:  # translate per paragraph
                                    f.write(self.__trans_parwise(content, translator))
                                else:
                                    f.write(self.__trans_linewise(content, translator))
                            else:
                                raise RuntimeError("Unknown chunk type detected, this is a bug")


    def __trans_linewise(self, content, translator):
        """Translate the chunk linewise."""
        lines = []
        for line in content.split('\n'):
            line_stripped = line.strip()
            trans_stripline = ''
            if line_stripped:
                trans_stripline = trans(translator, line_stripped) # translate the stripped version
            # and re-inject the stripped translation into original line (not stripped)
            lines.append(line.replace(line_stripped,
                        trans_stripline, 1))
        return '\n'.join(lines)


    def __trans_parwise(self, content, translator):
        """Extract translatable strings block-wise, query for translation of
        block and re-inject result."""
        result = []
        for paragraph in split_paragraphs(content):
            stripped = paragraph.strip('\n\r')
            paragraph = paragraph.replace(stripped, trans(translator,
                    stripped))
            result.append(paragraph)
        return '\n\n'.join(result)


    def on_after_build(self, builder, build_state, source, prog, **extra):
        if self.enabled and isinstance(source,Page):
            try:
                text = source.contents.as_text()
            except IOError:
                pass
            else:
                fields = source.datamodel.fields
                sections = dict(tokenize(text.splitlines())) # {'sectionname':[list of section texts]}
                self.process_node(fields, sections, source, source.datamodel.id, builder.env.root_path)


    def get_templates_pot_filename(self):
        try:
            return self.pot_templates_filename
        except AttributeError:
            self.pot_templates_file = tempfile.NamedTemporaryFile(suffix=".pot",prefix="templates-")
            self.pot_templates_filename = self.pot_templates_file.name
            return self.pot_templates_filename

    def on_before_build_all(self, builder, **extra):
        if self.enabled:
            reporter.report_generic("i18n activated, with main language %s"% self.content_language )
            templates_pot_filename = self.get_templates_pot_filename()
            reporter.report_generic("Parsing templates for i18n into %s" \
                    % relpath(templates_pot_filename, builder.env.root_path))
            translations.parse_templates(templates_pot_filename)
            # compile existing po files
            for language in self.translations_languages:
                po_file=POFile(language, self.i18npath)
                po_file.compile()
            # walk through contents.lr files and produce alternatives
            # before the build system creates its work queue
            self.translate_contents()


    def on_after_build_all(self, builder, **extra):
        """Once the build process is over :
        - write the translation template `contents.pot` on the filesystem,
        - write all translation contents+<language>.po files """
        if not self.enabled:
            return
        contents_pot_filename = join(builder.env.root_path, self.i18npath, 'contents.pot')
        pots = [contents_pot_filename,
                self.get_templates_pot_filename(),
                join(builder.env.root_path, self.i18npath, 'plugins.pot')]
        # write out contents.pot from web site contents
        translations.write_pot(pots[0], self.content_language)
        reporter.report_generic("%s generated" % relpath(pots[0],
            builder.env.root_path))
        pots = [p for p in pots if os.path.exists(p) ] # only keep existing ones
        if len(pots) > 1:
            translations.merge_pot(pots, contents_pot_filename)
            reporter.report_generic("Merged POT files %s" % ', '.join(
                relpath(p, builder.env.root_path) for p in pots))

        for language in self.translations_languages:
            po_file=POFile(language, self.i18npath)
            po_file.generate()
