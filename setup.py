# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup (
    name='live-life-tracker',
    version='0.0.1',
    packages=find_packages(),

    author='morytus',
    author_email='sundayjuice@gmail.com',

    url='https://github.com/morytus/live-life-tracker',
    description='Simple time tracker',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    python_requires='~=3.6',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python 3',
        'Programming Language :: Python 3.7',
        'Programming Language :: Python 3.8',
        'Programming Language :: Python 3.9',
        'Operationg System :: OS Independent',
    ],

    install_requires=[
        'Click~=8.0',
        'toml'
    ],

    package_data={'llt': ['data/*']},

    entry_points={
        'console_scripts': [
            'llt=llt.entry:main'
        ]
    }
)
