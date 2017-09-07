#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Convenience wrapper for running bootstrap directly from source tree."""

import sys

sys.path.insert(0, "/usr/lib/qpid-dispatch/python")

from qpid_dispatch_internal.management.qdrouter import QdSchema
from Jinja2Writer import Jinja2Writer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")
args = parser.parse_args()

class Configuration(Jinja2Writer):
    def run(self):
        self.entity_types_extending("configurationEntity")


def main():
    """Generate Jinja2 qdrouterd.conf template"""
    if args.output is not None:
        sys.stdout = open(args.output, 'w')

    Configuration(sys.stdout, QdSchema()).run()
