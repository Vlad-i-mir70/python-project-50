#!/usr/bin/env python3


def format_dict_to_string(dict):
    dict_to_str = str(dict)
    lower_str = dict_to_str.lower()
    lower_str_no_first_brace = lower_str.replace('{', ' ')
    lower_str_no_brace = lower_str_no_first_brace.replace('}', ' ')
    lower_str_no_quotes = lower_str_no_brace.replace("'", '')
    lower_str_split = lower_str_no_quotes.split(',')
    print(lower_str[0][0])
    for i in lower_str_split:
        print(i)
    print(lower_str[-1][-1])
    return dict_to_str
