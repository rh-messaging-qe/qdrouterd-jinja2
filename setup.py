# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
# install_reqs = parse_requirements('requirements.txt', session='hack')

# reqs is a list of requirement
# reqs = [str(ir.req) for ir in install_reqs]
# setup( ... install_requires=reqs, ...)

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
    long_description=open('README.md').read(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/rh-messaging-qe/qdrouterd-jinja2',
    author='Dominik Lenoch <dlenoch@redhat.com>, Jakub Stejskal <jstejska@redhat.com>',
    author_email='dlenoch@redhat.com'
)
