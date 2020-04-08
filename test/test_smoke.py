import lxml.etree as et
from . import validate


def test_smoke():
    xml = et.fromstring(b'''
<inno:dom xmlns:inno="http://innodatalabs.com/innodom">
<inno:content>
</inno:content>
</inno:dom>
''')
    validate(xml)
