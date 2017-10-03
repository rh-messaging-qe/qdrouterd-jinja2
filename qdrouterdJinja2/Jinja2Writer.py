#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from collections import namedtuple


class Jinja2Writer(object):
    """Write the schema as an Jinja2 template"""

    def __init__(self, output, schema, quiet=True, defaults=False):
        self.output = output
        self.schema = schema
        self.quiet = quiet
        self.defaults = defaults
        self._heading = 0

    def warn(self, message):
        if not self.quiet:
            print >> sys.stderr, message

    def write(self, text):
        self.output.write(text)

    def writeln(self, text=""):
        self.output.write(text + "\n")

    def para(self, text):
        self.write(text + "\n")

    def heading(self, text=None):
        if text:
            self.para("\n{%% if item.%s is defined %%}\n{%% for %s in item.%s %%}\n%s {" % (text, text, text, text))

    class Section(namedtuple("Section", ["writer", "heading"])):
        def __enter__(self):
            self.writer.heading(self.heading)

        def __exit__(self, ex, value, trace):
            self.writer.write('}\n{% endfor %}\n{% endif %}\n')

    def section(self, heading):
        self._heading = heading
        return self.Section(self, heading)

    def attribute_qualifiers(self, attr):
        default = attr.default
        if isinstance(default, str) and default.startswith('$'):
            default = None  # Don't show defaults that are references, confusing.

        # attr.required and "required",  @todo implement required
        # attr.unique and "unique",  @todo for loop
        if default and self.defaults:
            return "{%% else %%}    %s: %s" % (attr.name, default)
        else:
            return ''

    def attribute_type(self, attr):
        self.writeln("{%% if %s.%s is defined %%}    %s: {{ %s.%s }}%s{%% endif %%}\n" % (
            self._heading, attr.name, attr.name, self._heading, attr.name,
            self.attribute_qualifiers(attr)))

    def attribute_types(self, holder):
        for attr in holder.my_attributes:
            self.attribute_type(attr)

    def entity_type(self, entity_type):
        with self.section(entity_type.short_name):
            self.attribute_types(entity_type)

    def entity_types_extending(self, base_name):
        base = self.schema.entity_type(base_name)
        for entity_type in self.schema.filter(lambda t: t.extends(base)):
            self.entity_type(entity_type)
