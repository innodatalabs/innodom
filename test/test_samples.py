import lxml.etree as et
from . import res, validate


def test01():

    with open(res('sample01.xml'), 'rb') as f:
        xml = et.fromstring(f.read())

    validate(xml)


def test02():

    with open(res('sample02.xml'), 'rb') as f:
        xml = et.fromstring(f.read())

    validate(xml)
