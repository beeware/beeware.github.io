.. image:: http://beeware.org/static/images/brutus-270.png
    :width: 72px
    :target: https://beeware.org

beeware.github.io
=================

This is the homepage for the `BeeWare project`_.

It is a `Lektor`_-based site.

If you want to contribute a modification, you can fork this repository and
submit a pull request. However, **do not fork the master branch** - fork the
`lektor branch`_ and make changes there instead.

.. _lektor branch: https://github.com/beeware/beeware.github.io/tree/lektor

If you want to test out a change before you submit it, download and install
`Lektor`_ (note: currently it's better to use Lektor with Python 2.7):

    $ pip install lektor

Then from the root directory of the checkout, run:

    $ lektor server

.. _Lektor: https://getlektor.com

This will `start a webserver`_ that will autoreload whenever you make a change
to site content.

.. _start a webserver: http://127.0.0.1:5000

Community
---------

You can talk to the community through:

* `@pybeeware on Twitter`_

* BeeWare Gitter channel: `beeware/general`_

* `Tickets on the beeware.github.io issue tracker`_

Contributing
------------

If you find problems with this website, `log them on GitHub`_. If you
want to contribute, please `fork the code`_ and `submit a pull request`_.

Before submitting a pull request, please make sure your forked branch is up
to date with the original branch. To do this:

- set your upstream remote::

    $ git remote add upstream https://github.com/beeware/beeware.github.io.git

- make sure you have the latest changes from upstream::

    $ git fetch upstream

- rebase your **lektor** branch to **upstream** before pushing to git and
  submitting a pull request::

    $ git rebase upstream/lektor


.. _BeeWare project: http://beeware.org
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _beeware/general: https://gitter.im/beeware/general
.. _Tickets on the beeware.github.io issue tracker: https://github.com/beeware/beeware.github.io/issues
.. _log them on Github: https://github.com/beeware/beeware.github.io/issues
.. _fork the code: https://github.com/beeware/beeware.github.io/tree/lektor
.. _submit a pull request: https://github.com/beeware/beeware.github.io/pulls


Translating
-----------

Want to make BeeWare more accessible to non-English-speakers?  Help translate the site!  Steps are as follows:

1. Add language specification to `BeeWare.lektorproject <https://github.com/beeware/beeware.github.io/blob/lektor/BeeWare.lektorproject>`_.

   Fill out the name of the language, its url prefix, and the locale. Make sure you use the correct `ISO 639-1 <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ locale code - for many countries, it's not the same as
   the national TLD. For example, the ISO 639-1 Danish locale is 'da', but Denmark uses the '.dk' TLD.

2. Add an entry for your language to the `Atom configuration <https://github.com/beeware/beeware.github.io/blob/lektor/configs/atom.ini>`_.

3. Add your first translation, by translating the names for the menus at the top of each page. Edit `the menus translation file <https://github.com/beeware/beeware.github.io/blob/lektor/databags/menu.ini>`_, adding a block for your language.

4. Start adding translations for content pages ont he site. Translated files are at the same directory level as the primary English files, but have a language suffix. For example, Arabic's locale is 'ar', so you would add `contents+ar.lr` wherever the original file name is `contents.lr`

A great place to start translating is the `contributing section <beeware.github.io/content/contributing>`_.
