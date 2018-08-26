#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = []


setup(
    author="Zsolt Ero",
    author_email='zsolt@hyperknot.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Simply manage git tags.",
    entry_points={
        'console_scripts': [
            'gittag=gittag.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='gittag git tag',
    name='gittag',
    packages=find_packages(include=['gittag']),
    setup_requires=setup_requirements,
    url='https://github.com/hyperknot/gittag',
    version='0.1.0',
    zip_safe=False,
)
