# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to pybee site."""

# Third party imports
from setuptools import setup


setup(
    name='lektor-pybee-plugin',
    author='Gonzalo Peña-Castellanos',
    author_email='goanpeca@gmail.com',
    url='https://github.com/beeware/beeware.github.io/tree/lektor/packages/lektor_pybee_plugin',
    version='0.1',
    license='MIT',
    py_modules=['lektor_pybee_plugin'],
    install_requires=['Lektor', 'MarkupSafe', 'Pygments'],
    entry_points={
        'lektor.plugins': [
            'pybee-plugin = lektor_pybee_plugin:PyBeePlugin',
        ]
    }
)
