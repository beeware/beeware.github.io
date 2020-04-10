# -*- coding: utf-8 -*-
# This is an updated copy of lektor-atom plugin
# which replaces the deprecated Werkzeug's atom with Pelican's feedgenerator.

from setuptools import setup

setup(
    author=u'A. Jesse Jiryu Davis',
    author_email='jesse@emptysquare.net',
    install_requires=['MarkupSafe', 'feedgenerator'],
    keywords='Lektor plugin static-site blog atom rss',
    license='MIT',
    name='lektor-atom',
    py_modules=['lektor_atom'],
    url='https://github.com/nixjdm/lektor-atom',
    version='0.4.0',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Lektor',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'lektor.plugins': [
            'atom = lektor_atom:AtomPlugin',
        ]
    }
)
