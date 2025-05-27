# Lektor i18n plugin

**This version of the plugin is a modified copy of the updated version used by [The Tor Project](https://gitlab.torproject.org/tpo/web/lego/-/blob/main/packages/i18n/lektor_i18n.py).**

This plugin enables a smarter way to translate a [Lektor](http://getlektor.com) static website using old-good PO files. So you can use your beloved translation processes and tools.

## Principles

The idea of this plugin is to capture the **sentences** or **paragraphs** from your **content** and **templates**, and populate a standard *Gettext* [PO file](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html). Using usual tools, user can translate these files, very easily. Then the plugin will merge the translations into new [_alternative_](https://www.getlektor.com/docs/content/alts/) content files, providing a translated website.

## Configuration

### Configuration file

#### `configs/i18n.ini`

    content = en
    translations = fr,es,it
    i18npath = i18n
    translate_paragraphwise = False
    url_prefix = https://website_url/


Where :

* `content` is the language used to write `contents.lr` files (default is `en`)
* `translations` is the list of target languages (you want to translate into).
* `i18npath` is the directory where translation files will be produced/stored (default is `i18n`). This directory needs to be relative to root path.
* `translate_paragraphwise` specifies whether translation strings are created per line or per paragraph. The latter is helpful for documents wrapping texts at 80 character boundaries. It is set to `False` by default.
* `url_prefix` is the final url of your lektor website. This provides translators with a way to see the strings in context.

#### `babel.cfg`

If you plan to localise your templates as well, you can use
`{{ _("some string") }}` in your templates. To make this work, babel for Python should be installed (pip install babel; maybe pip3). A `babel.cfg` also has to exist in your project root with this content:

    [jinja2: **/templates/**.html]
    encoding = utf-8
    extensions=jinja2.ext.autoescape,jinja2.ext.with_

### Translatable fields

In order for a field to be marked as translatable, an option has to be set in the field definition. Both blocks and flowblocks fields are subjects to translations.

in `flowblocks/*.ini` and/or `models/*.ini`, mark a field as translatable with :

    [model]
    name = Page
    label = {{ this.title }}

    [fields.title]
    label = Title
    type = string
    translate = True

    [fields.body]
    label = Body
    type = markdown
    translate = True

Both `title` and `body` are now translatable. It means that during the parsing phase, all sentences from `title` or `body` fields from the `contents.lr` files with `Page` model will populate the collected PO file.

Another flowblock example:

    [block]
    name = Section Block
    button_label = Section

    [fields.title]
    label = Title
    type = string
    translate = True

    [fields.body]
    label = Body
    type = markdown
    translate = True

    [fields.image]
    label = Image
    type = select
    source = record.attachments.images

    [fields.image_position]
    label = Image Position
    type = select
    choices = left, right
    choice_labels = Left, Right
    default = right

Here again, `body` and `title` will be translated. But `image` and `image_position` won't.

### Non-english content

Thanx to a limitation of msginit it's not so easy to translate a website with default language set to anything but english.

So if your default content language is not english, you will have to edit the first `contents-en.po` file and remove the translations (by hand ?)...

## Installation

### Prerequisites

#### Lektor

This plugin has been tested with `Lektor 3..0.x`.

#### GetText

Both Gettext and Pybabel are required.  For a Debian/Ubuntu system, this means a simple :

    sudo apt-get install gettext python3-babel

On macOS, use a decent package manager, like MacPorts or Homebrew. With Homebrew:

    brew install gettext

and then pip to fetch pybabel:

    pip install babel

### Installation

Very straightforward :

    $ lektor plugins add lektor-i18n

Verify installation with a simple :

    $ lektor plugins list
    ...
    lektor-i18n (version 0.1)
    ...

## Usage

The translation mechanism is hooked into the build system. So translating a website just means building the website.

    $ lektor build

On first call, a new `i18n` directory (can be changed in configuration file) will be created on top the lektor tree.

This directory will be populated with a single `contents.pot` file, compiling all the sentences found by the plugin. The list of fields eligible to translation is configured in the models/flows definition with `translate=True` added to each field.

For each translation language (still from the configuration file), a `content-<language>.po` file will be created/updated. These are the files that need to be translated with your prefered tool (like [POEdit](http://poedit.net) or [Transifex](http://transifex.com)).

All translation files (`contents-*.po`) are then compiled and merged with the original `contents.lr` files to produce all the `contents-<language>.lr` files in their respective directories.

Due to the way Lektor building system is designed, all these steps happen on every build. This means that sometime, after translating the `contents-*.po` files, it might be required to run the build system twice to see the translation appear in the final HTML files.

### Project file

It's still the user responsability to modify the project file in order to include the expected languages :

    [alternatives.en]
    name = English
    primary = yes
    locale = en_US

    [alternatives.fr]
    name = French
    url_prefix = /fr/
    locale = fr

See [Lektor Documentation](https://www.getlektor.com/docs/content/alts/) for more information.

## Support

This plugin is provided as-is by [NumeriCube](http://numericube.com) a human-sized Paris-based company prodiving tailored services to smart customers.

We will be happy to try to help you with this plugin if need. Just file an issue on our [GitHub account](https://gihub.com/numericube/lektor-i18n-plugin/).

