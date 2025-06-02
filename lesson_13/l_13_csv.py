import csv
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)
    

def write_csv(filepath: Path, content:list):
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";") #quoting=csv.QUOTE_ALL
        writer.writerows(content)


if __name__ == "__main__":
    my_csv = Path(__file__).parent / "new.csv"
    content = read_file(my_csv)
    print(content, type(content))
    my_csv_2 = Path(__file__).parent / "new2.csv"
    write_csv(my_csv_2, content)