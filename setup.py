from setuptools import setup, find_packages

setup(
    name="pwgen_princ",
    version="1.0.0",
    packages=find_packages(),
    description="Advanced password generator with strength scoring and HTML reports",
    author="Prince Mokgwadi",
    entry_points={
        'console_scripts': [
            'pwgen = pwgen_princ.pwgen.main:main',

        ],
    },
)
