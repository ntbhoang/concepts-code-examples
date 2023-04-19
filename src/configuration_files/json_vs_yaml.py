import json
import yaml


def read_json(file_path: str):
    with open(file_path, "r") as f:
        return json.load(f)


def read_yaml(file_path: str):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


print(read_json("/Users/hoangntb/PycharmProjects/concepts-code-examples/src/configuration_files/test_data.json")
      ['APP']['ENVIRONMENT'])

print(read_yaml("/Users/hoangntb/PycharmProjects/concepts-code-examples/src/configuration_files/test_data.yaml")
      ['APP']['ENVIRONMENT'])