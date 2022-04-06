# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to BeeWare site."""

# Standard library imports
from datetime import datetime
import os
import subprocess
import sys
from urllib.parse import quote_plus

# Third party imports
from lektor.pluginsystem import Plugin
from lektor.db import Record
from markupsafe import Markup
from pygments import highlight
from pygments import lexers
from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles


PY3 = sys.version_info[0] == 3


class BeeWarePlugin(Plugin):
    name = 'BeeWare Custom Lektor Plugin'
    description = 'This is a custom local plugin to add extra functionality.'

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    EXECUTE_CACHE = {}

    def on_setup_env(self, **extra):

        # --- Helper methods
        # ---------------------------------------------------------------------
        def execute(cmd):
            """Execute a cmd (list) and return the stdout and stderr."""
            joined_cmd = ' '.join(cmd)
            if joined_cmd in self.EXECUTE_CACHE:
                stdout, stderr = self.EXECUTE_CACHE[joined_cmd]
            else:
                stdout, stderr = None, None
                try:
                    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                    stdout, stderr = p.communicate()

                    if PY3:
                        if stdout:
                            stdout = stdout.decode()
                        if stderr:
                            stderr = stderr.decode()

                except OSError:
                    print('\nCommand not found!\n')
                    print(joined_cmd)
                    print('\n')
                except Exception as e:
                    print(e)
                    print('\n')

                self.EXECUTE_CACHE[joined_cmd] = (stdout, stderr)

            return stdout, stderr

        def git_commits(filepath, since):
            """Get git commit hashes for `filepath` `since` a given date."""
            cmd = ('git', 'log', '--since="'+since+'"', '--pretty=format:%H',
                   '--', filepath)
            stdout, stderr = execute(cmd)

            commits = []
            if stdout:
                commits = [c for c in stdout.split('\n') if c]

            return commits

        def git_diff(filepath, since):
            """Get git diff for a given `filepath` `since` a given date."""
            html_diff = None
            commits = git_commits(filepath, since)
            if commits:
                cmd = ('git', '--no-pager', 'diff', commits[-1]+'^', '--',
                       filepath)
                stdout, stderr = execute(cmd)

                if stdout:
                    html_diff = highlight(stdout, lexers.DiffLexer(),
                                          HtmlFormatter())

                    # print(' '.join(cmd))
                    # print(diff)
                    # print('\n')

            return html_diff

        def git_modified_date(filepath):
            """Get last modified date of `filepath` from git."""
            git_mod_date = None

            if os.path.isfile(filepath):
                cmd = ('git', 'log', '-1',
                       '--date=format:"'+self.DATE_FORMAT+'"',
                       '--format="%ad"', filepath)
                stdout, stderr = execute(cmd)

                if stdout:
                    stdout = stdout.split('\n')[0]
                    stdout = stdout.replace('"', '')
                    stdout = stdout.replace("'", '')

                if stdout:
                    git_mod_date = datetime.strptime(stdout, self.DATE_FORMAT)

            # print(' '.join(cmd))
            # print(git_mod_date)
            # print('\n')

            return git_mod_date

        # --- Exposed methods
        # ---------------------------------------------------------------------
        def get_pygments_css_styles(style='default'):
            """Get pygments CSS."""
            class_name = '.highlight'
            css = None
            if style in get_all_styles():
                cmd = ('pygmentize', '-S', style, '-f', 'html', '-a',
                       class_name)
                stdout, stderr = execute(cmd)
                css = '<style>{}</style>'.format(stdout)

            return css

        def is_alt_outdated(record):
            """Check if record alternative is outdated."""
            return _alt_outdated_diff(record, return_diff=False)

        def alt_outdated_diff(record):
            """Check if record alternative is outdated and returns the diff."""
            return _alt_outdated_diff(record, return_diff=True)

        def _alt_outdated_diff(record, return_diff=True):
            """Check if record alternative is outdated and returns the diff."""
            if not isinstance(record, Record):
                raise ValueError('Must provide a `Record` object')

            config = self.env.jinja_env.globals['config']
            site = self.env.jinja_env.globals['site']
            primary_path = site.get(record.path, alt="_primary").contents.filename
            primary_path = primary_path.replace(
                '+{0}.lr'.format(config.primary_alternative), '.lr')
            try:
                alt_path = record.contents.filename
                alt_text = '+{0}.lr'.format(config.primary_alternative)
                if alt_text in alt_path:
                    alt_path = alt_path.replace(alt_text, '.lr')
            except IOError:
                # This means the alt content file does not exist
                alt_path = None

            primary_modtime = None
            if os.path.isfile(primary_path):
                # primary_modtime = os.path.getmtime(primary_path)
                primary_modtime = git_modified_date(primary_path)

            alt_modtime = None
            if os.path.isfile(alt_path):
                # alt_modtime = os.path.getmtime(alt_path)
                alt_modtime = git_modified_date(alt_path)

            diff = None
            if alt_modtime and primary_modtime > alt_modtime and return_diff:
                diff = git_diff(primary_path,
                                alt_modtime.strftime(self.DATE_FORMAT))

            if not return_diff:
                diff = alt_modtime and primary_modtime > alt_modtime

            return diff

        def urlencode_limit(string, limit=6000):
            """Encodes url for uri but if over limit returns None."""
            if type(string) == 'Markup':
                string = string.unescape()

            if len(string) <= limit:
                string = string.encode('utf8')
                string = quote_plus(string)
                string = Markup(string)
            else:
                string = None

            return string

        # Add additional methods to the environment globlas
        self.env.jinja_env.globals.update(is_alt_outdated=is_alt_outdated)
        self.env.jinja_env.globals.update(alt_outdated_diff=alt_outdated_diff)
        self.env.jinja_env.globals.update(urlencode_limit=urlencode_limit)
        self.env.jinja_env.globals.update(
            get_pygments_css_styles=get_pygments_css_styles)

        # Add some python builtins that are good for debugging
        self.env.jinja_env.globals.update(dir=dir)
