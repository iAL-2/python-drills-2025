from paths import DATA_DIR
import csv

def csvmini():
    ash = [("Alice", 25), ("Bob", 30), ("Carol", 22)]
    with open(DATA_DIR / "test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        for name, age in ash:
            writer.writerow([name,age])


import csv
from paths import DATA_DIR

def csvWriter():
    d = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Carol", "age": 30},
    ]
    with open(DATA_DIR/"test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        for dict in d:
            writer.writerow([dict["name"], dict["age"]])
    with open(DATA_DIR/"test.csv", "r", encoding="utf-8") as f:
        return f.read()
    
def csvWriter():
    d = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Carol", "age": 30},
    ]
    with open(DATA_DIR/"test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(d)