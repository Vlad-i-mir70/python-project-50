#!/usr/bin/env python3
from gendiff.cli import args
from gendiff.generate_diff import generate_diff
from gendiff.format_dict_to_str import format_dict_to_string


def main():
    format_dict_to_string(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
