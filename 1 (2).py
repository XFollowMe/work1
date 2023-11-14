import json

file = "input.json"

def task() -> float:
    with open(file,"r") as a:
        text = json.load(a)

        sums = sum([item["score"] * item["weight"] for item in text])
        return (f"{sums:.3f}")
print(task())
