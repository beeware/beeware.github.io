.. image:: http://pybee.org/static/images/brutus-270.png
    :width: 72px
    :target: https://pybee.org

pybee.github.io
===============

This is the homepage for the `BeeWare project`_.

It is a `Lektor`_-based site.

.. _Lektor: https://getlektor.com

If you want to contribute a modification, you can fork this repository and
submit a pull request. However, **do not fork the master branch** - fork the
`lektor branch`_ and make changes there instead.

.. _lektor branch: https://github.com/pybee/pybee.github.io/tree/lektor

If you want to test out a change before you submit it, download and install
Lektor; then from the root directory of the checkout, run:

    $ lektor server

This will `start a webserver`_ that will autoreload whenever you make a change
to site content.

.. _start a webserver: http://127.0.0.1:8000

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
