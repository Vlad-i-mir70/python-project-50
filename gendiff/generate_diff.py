import json
import yaml


def generate_diff(file_path1, file_path2):

    if file_path1.endswith('.yaml'):
        first_file_opened_yaml = yaml.safe_load(open(file_path1))
        second_file_opened_yaml = yaml.safe_load(open(file_path2))
        for i in first_file_opened_yaml:
            first_file_opened = i
        for z in second_file_opened_yaml:
            second_file_opened = z
    else:
        first_file_opened = json.load(open(file_path1))
        second_file_opened = json.load(open(file_path2))

    result = {}
    dict_not_in_second_file = dict([x for x in first_file_opened.items() if x not in second_file_opened.items()])
    dict_not_in_first_file = dict([x for x in second_file_opened.items() if x not in first_file_opened.items()])
    dict_in_first_and_second_file = dict([x for x in second_file_opened.items() if x in first_file_opened.items()])
    for k, v in dict_not_in_second_file.items():
        new_key = f'- {k}'
        result[new_key] = v
    for k, v in dict_not_in_first_file.items():
        new_key = f'+ {k}'
        result[new_key] = v
    for k, v in dict_in_first_and_second_file.items():
        new_key = f'  {k}'
        result[new_key] = v
    sorted_result = dict(sorted(result.items(), key=lambda x: x[0][2:]))
    return sorted_result
