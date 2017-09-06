import sys
from qpid_dispatch_internal.management.qdrouter import QdSchema
from generator import Jinja2Writer


class Configuration(Jinja2Writer):
    def run(self):
        self.entity_types_extending("configurationEntity")


def main():
    """Generate Jinja2 qdrouterd.conf template"""
    Configuration(sys.stdout, QdSchema()).run()


if __name__ == '__main__':
    main()
