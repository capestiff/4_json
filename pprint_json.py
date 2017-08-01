import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def pretty_print_json(data):
    print(json.dumps(json.loads(data), indent=4, ensure_ascii=False))


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_file", help='program reads JSON file and prints the content')
    args = parser.parse_args()
    return args.path_to_file

if __name__ == '__main__':
    path_to_file = parse_cli_args()

    json_data = load_data(path_to_file)
    pretty_print_json(json_data)
    with open('json.txt', 'w') as f:
        f.write(json.dumps(json.loads(json_data), indent=4, ensure_ascii=False))
