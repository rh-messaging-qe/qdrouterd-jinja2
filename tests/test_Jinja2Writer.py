import sys
import os.path

import unittest
import pytest

from StringIO import StringIO
from qdrouterdJinja2.Jinja2Writer import Jinja2Writer
from qpid_dispatch_internal.management.qdrouter import QdSchema
# from pkgutil import get_data


class SimplisticTest(unittest.TestCase):

    # def test_Jinja2Writer(self):
    #     stdout = sys.stdout
    #     sys.stdout = StringIO()
    #     Jinja2Writer(stdout, QdSchema(conf_path='%s/json' % get_data(os.path.dirname(__file__), 'qdrouter.json')),
    #                  defaults=False).entity_types_extending("configurationEntity")
    #     sys.stdout = stdout
    #     self.assertIsNotNone(sys.stdout)
    #

    def test(self):
        pass
