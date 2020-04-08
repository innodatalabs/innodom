import os
import lxml.etree as et

def schema_file_name():
    return os.path.join(os.path.dirname(__file__), '../innodom.xsd')


def test_smoke():
    with open(schema_file_name(), 'rb') as f:
        schema = et.XMLSchema(et.fromstring(f.read()))

    xml = et.fromstring(b'''
<inno:dom xmlns:inno="http://innodatalabs.com/innodom">
</inno:dom>
''')

    schema.validate(xml)