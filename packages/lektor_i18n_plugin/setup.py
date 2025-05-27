from setuptools import setup

setup(
    name='lektor-i18n',
    version='0.4.4',
    author=u'NumeriCube',
    author_email='support@numericube.com',
    url='https://github.com/numericube/lektor-i18n-plugin',
    license='GPL',
    py_modules=['lektor_i18n'],
    entry_points={
        'lektor.plugins': [
            'i18n = lektor_i18n:I18NPlugin',
        ]
    }
)
