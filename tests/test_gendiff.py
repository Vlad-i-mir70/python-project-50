from gendiff.generate_diff import generate_diff
import json

def test_file_download():
    file_path1 = json.load(open('file1.json'))
    assert file_path1 == {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}



def test_generate_diff():   
    result = generate_diff('file3.json', 'file4.json')
    assert result == {'  test': 'one'}

   
def test_generate_diff2():   
    result = generate_diff('file1.json', 'file2.json')
    assert result == {'- follow': False, '  host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True}
