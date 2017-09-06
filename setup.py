from setuptools import setup, find_packages

setup(
    name='qdrouterd-jinja2',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='Apache 2.0',
    description='Generate Jinja2 template from qpid-dispatch',
    long_description=open('README.md').read(),
    install_requires=[''],
    url='https://github.com/rh-messaging-qe/qdrouterd-jinja2',
    author='Dominik Lenoch <dlenoch@redhat.com>, Jakub Stejskal <jstejska@redhat.com>',
    author_email='dlenoch@redhat.com'
)
