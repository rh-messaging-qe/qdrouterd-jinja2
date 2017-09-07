#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Convenience wrapper for running bootstrap directly from source tree."""

import sys
from collections import namedtuple


class Jinja2Writer(object):
    """Write the schema as an Jinja2 template"""

    def __init__(self, output, schema, quiet=True):
        self.output, self.schema, self.quiet = output, schema, quiet
        self._heading = 0
        # Options affecting how output is written

    def warn(self, message):
        if not self.quiet:
            print >> sys.stderr, message

    def write(self, text):
        self.output.write(text)

    def writeln(self, text=""):
        self.output.write(text + "\n")

    def para(self, text):
        self.write(text + "\n")

    def heading(self, text=None, sub=0):
        if text:
            self.para("\n{%% for %s in item.%s %%}\n%s {" % (text, text, text))

    class Section(namedtuple("Section", ["writer", "heading"])):
        def __enter__(self):
            self.writer.heading(self.heading, sub=+1)

        def __exit__(self, ex, value, trace):
            self.writer.heading(sub=-1)
            self.writer.write('}\n{% endfor %}\n')

    def section(self, heading):
        self._heading = heading
        return self.Section(self, heading)

    @staticmethod
    def attribute_qualifiers(attr, show_create=True, show_update=True):
        default = attr.default
        if isinstance(default, basestring) and default.startswith('$'):
            default = None  # Don't show defaults that are references, confusing.

        # attr.required and "required",  @todo implement required
        # attr.unique and "unique",  @todo for loop
        return "{%% else %%}%s: %s" % (attr.name, default)

    def attribute_type(self, attr, holder=None, show_create=True, show_update=True):
        self.writeln("{%% if %s.%s %%}    %s: {{ %s.%s }} %s{%% endif %%}" % (
            self._heading, attr.name, attr.name, self._heading, attr.name,
            self.attribute_qualifiers(attr, show_create, show_update)))

    def attribute_types(self, holder):
        for attr in holder.my_attributes:
            self.attribute_type(attr, holder)

    def entity_type(self, entity_type, operation_defs=True):
        with self.section(entity_type.short_name):
            self.attribute_types(entity_type)

    def entity_types_extending(self, base_name):
        base = self.schema.entity_type(base_name)
        for entity_type in self.schema.filter(lambda t: t.extends(base)):
            self.entity_type(entity_type)
