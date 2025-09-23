from paths import DATA_DIR
import csv

def csvmini():
    ash = [("Alice", 25), ("Bob", 30), ("Carol", 22)]
    with open(DATA_DIR / "test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        for name, age in ash:
            writer.writerow([name,age])