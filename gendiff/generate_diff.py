import json


def generate_diff(file_path1, file_path2):

    first_file_opened = json.load(open(file_path1))
    secopnd_file_opened = json.load(open(file_path2))
    result = {}
    dict_not_in_second_file = dict([x for x in first_file_opened.items() if x not in secopnd_file_opened.items()])
    dict_not_in_first_file = dict([x for x in secopnd_file_opened.items() if x not in first_file_opened.items()])
    dict_in_first_and_second_file = dict([x for x in secopnd_file_opened.items() if x in first_file_opened.items()])
    for k, v in dict_not_in_second_file.items():
        new_key = f'- {k}'
        result[new_key] = v
    for k, v in dict_not_in_first_file.items():
        new_key = f'+ {k}'
        result[new_key] = v
    for k, v in dict_in_first_and_second_file.items():
        new_key = f'  {k}'
        result[new_key] = v
    sorted_result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    print(sorted_result)
