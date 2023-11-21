import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        file = [string for string in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, "w") as r:
        r.write(json.dumps(file, indent=4))


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
          print(line, end="")