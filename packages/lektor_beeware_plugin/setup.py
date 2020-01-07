# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to BeeWare site."""

# Third party imports
from setuptools import setup


setup(
    name='lektor-beeware-plugin',
    author='Gonzalo Peña-Castellanos',
    author_email='goanpeca@gmail.com',
    url='https://github.com/beeware/beeware.github.io/tree/lektor/packages/lektor_beeware_plugin',
    version='0.1',
    license='MIT',
    py_modules=['lektor_beeware_plugin'],
    install_requires=['Lektor', 'MarkupSafe', 'Pygments'],
    entry_points={
        'lektor.plugins': [
            'beeware-plugin = lektor_beeware_plugin:BeeWarePlugin',
        ]
    }
)
