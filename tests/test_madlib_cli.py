
from madlib_cli import __version__
from madlib_cli.madlib_cli import read_template , parse, merge 

import pytest

"""
to skip any test you can use formula before the test :

@pytest.mark.skip(reason=" still working on it")
and import pytest above 
** for detailed test use pytest -v
"""


def test_version():
    assert __version__ == '0.1.0'


def testRead():
    expected = open("assets/template.txt",'r').read()
    received = read_template()
    assert expected == received

def testParse():
    expected = ["first name","age"]
    received = parse("hello {first name}, I am {age} years old")
    assert expected == received


## merge takes empty curly braces
def testMerge():
    words = ['smart' , 'boxes', 'hungry' , 'eat']
    text = 'A {} {} had a {} dog so they {} them'
    received = merge(text, words)
    expected = 'A smart boxes had a hungry dog so they eat them'
    assert expected == received