import json
from pathlib import Path


def read_file(filepath: Path) -> dict:
    with open(filepath, "r", encoding="utf-8") as file:
        try:
            content = json.load(file)
        except json.decoder.JSONDecodeError:
            content = ""
        return content


def write_json(filepath: Path, content:dict):
    with open(filepath, "w", encoding="utf-8", ) as file:
        json.dump(content, file, indent=4)


if __name__ == "__main__":
    my_json = Path(__file__).parent / "test_result.json"
    content = read_file(my_json)
    print(content, type(content))
    json_string = '{"name": "Ivan", "age": 25, "city": "Kyiv", "pass": 95, "skip": 5,  "failed": 0, "is_failed": true}'
    json_to = json.loads(json_string)
    print(json_to)
    new_json = Path(__file__).parent / "new.json"
    write_json(new_json, json_to)