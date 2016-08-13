# -*- coding: utf -8*-
from setuptools import setup

setup(
    name="mailroom",
    description="This package allows the user to update an existing list of"
                "donors, to generate a Thank-You Letter,"
                "and to create a report",
    version=0.1,
    license='MIT',
    author="Alex German, Tatiana Weaver",
    author_email="Alexgerman11233@gmail.com, tanya83@uw.edu",
    py_modules=['mailroom'],
    package_dir={' ': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    entry_points={
        'console_scripts': [
            'mailroom=src.mailroom:main_function'
        ]
    }
)
