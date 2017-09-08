# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

from setuptools import setup

setup(
    name='qdrouterd-jinja2',
    version='0.1.1',
    packages=['qdrouterdJinja2'],
    entry_points={
        "console_scripts": ['qdrouterdJinja2 = qdrouterdJinja2.qdrouterdJinja2:main']
    },
    license='Apache 2.0',
    description='Generate qpid-dispatch config (qdrouterd.conf) as Jinja2 template from already'
                ' installed qpid-dispatch.',
    long_description=open('README.md').read().decode("utf-8"),
    install_requires=[''],
    url='https://github.com/rh-messaging-qe/qdrouterd-jinja2',
    author='Dominik Lenoch <dlenoch@redhat.com>, Jakub Stejskal <jstejska@redhat.com>',
    author_email='dlenoch@redhat.com'
)
