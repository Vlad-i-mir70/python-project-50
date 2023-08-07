from gendiff.generate_diff import generate_diff
from gendiff.format_dict_to_str import format_dict_to_string
#from gendiff.cli import args

import json
import pytest

@pytest.fixture

def file_path1():
    return {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}

def file_path2():
    return {
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}

#def test_file_download():
   # file_path1 = json.load(open('file1.json'))
   # assert file_path1 == {
 # "host": "hexlet.io",
 # "timeout": 50,
 # "proxy": "123.234.53.22",
  #"follow": False
#}



#def test_generate_diff():   
   # result = generate_diff('file3.json', 'file4.json')
    #assert result == {'  test': 'one'}

   
#def test_generate_diff2():   
    #result = generate_diff(file_path1, file_path2)
    #assert result == {'- follow': False, '  host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True}

def test_generate_diff2():   
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert result == {'- follow': False, '  host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True}

#def test_format_dict_to_string():
    result2 = test_dict = format_dict_to_string({'one':'two'})

    assert result2 == {'one':'two'}
