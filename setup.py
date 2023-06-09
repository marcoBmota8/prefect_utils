#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Marco Barbero Mota",
    author_email='marco.barbero.mota@vanderbilt.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This package compiles a series of utils that come handy when deploying tasks and flows using prefect 2.0.",
    entry_points={
        'console_scripts': [
            'prefect_utils=prefect_utils.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='prefect_utils',
    name='prefect_utils',
    packages=find_packages(include=['prefect_utils', 'prefect_utils.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/marcoBmota8/prefect_utils',
    version='0.0.1',
    zip_safe=False,
)
