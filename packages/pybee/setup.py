from setuptools import setup

setup(
    name='lektor-pybee',
    version='0.1',
    author='Tzu-ping Chung',
    author_email='uranusjr@gmail.com',
    license='MIT',
    py_modules=['lektor_pybee'],
    entry_points={
        'lektor.plugins': [
            'pybee = lektor_pybee:PyBeePlugin',
        ]
    }
)
