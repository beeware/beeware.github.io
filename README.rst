.. image:: http://pybee.org/static/images/brutus-270.png
    :width: 72px
    :target: https://pybee.org

pybee.github.io
===============

This is the homepage for the `BeeWare project`_.

It is a `Lektor`_-based site.

Installing development environment
------------------------------------

If you want to contribute a modification, you can fork this repository and
submit a pull request. However, **do not fork the master branch** - fork the
`lektor branch`_ and make changes there instead.

.. _lektor branch: https://github.com/pybee/pybee.github.io/tree/lektor

Using pip
~~~~~~~~~~

If you want to test out a change before you submit it, download and install
`Lektor`_ (note: currently it's better to use Lektor with Python 2.7):

    $ pip install lektor


Using pipenv
~~~~~~~~~~~~

If you use `pipenv`_, a .Pipfile is provided that has Lektor and Python 2.7
specified. From the root directory of the checkout, run:

    $ pipenv install

.. _pipenv: https://github.com/pypa/pipenv

Then to activate a shell that will use the virtual environment you created, run:

    $ pipenv run lektor server

Running the local server
------------------------

After you have installed Lektor using pip or pipenv change to the root directory
of the checkout, then run:

    $ lektor server

.. _Lektor: https://getlektor.com

This will `start a webserver`_ that will autoreload whenever you make a change
to site content. Note: the previous link will not work if your attempt
to start a webserver failed.

.. _start a webserver: http://127.0.0.1:5000

Community
---------

You can talk to the community through:

* `@pybeeware on Twitter`_

* BeeWare Gitter channel: `pybee/general`_

* `Tickets on the pybee.github.io issue tracker`_

Contributing
------------

If you find problems with this website, `log them on GitHub`_. If you
want to contribute, please `fork the code`_ and `submit a pull request`_.

Before submitting a pull request, please make sure your forked branch is up
to date with the original branch. To do this:

- set your upstream remote::

    $ git remote add upstream https://github.com/pybee/pybee.github.io.git

- make sure you have the latest changes from upstream::

    $ git fetch upstream

- rebase your **lektor** branch to **upstream** before pushing to git and
  submitting a pull request::

    $ git rebase upstream/lektor


.. _BeeWare project: http://pybee.org
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _pybee/general: https://gitter.im/pybee/general
.. _Tickets on the pybee.github.io issue tracker: https://github.com/pybee/pybee.github.io/issues
.. _log them on Github: https://github.com/pybee/pybee.github.io/issues
.. _fork the code: https://github.com/pybee/pybee.github.io/tree/lektor
.. _submit a pull request: https://github.com/pybee/pybee.github.io/pulls


Translating
-----------

Want to make BeeWare more accessible to non-English-speakers?  Help translate the site!  Steps are as follows:

1. Add language specification to:

	pybee.github.io/BeeWare.lektorproject

   Fill out the name of the language, its url prefix, and the locale.

2. Add translated mirror files at the same directory level as the primary English files  and add appropriate suffixes.

	For example:

		Arabic's locale is 'ar', so you would add...

		contents+ar.lr

		...where the original file name is:

		contents.lr

Note: A great place to start translating is the contributing section:

	pybee.github.io/content/contributing
