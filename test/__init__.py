import os
import lxml.etree as et

def res(*av):
    return os.path.join(os.path.dirname(__file__), 'resources', *av)


SCHEMA_FNAME = os.path.join(os.path.dirname(__file__), '../innodom.xsd')

def validate(xml):
    with open(SCHEMA_FNAME, 'rb') as f:
        schema = et.XMLSchema(et.fromstring(f.read()))
    schema.assertValid(xml)