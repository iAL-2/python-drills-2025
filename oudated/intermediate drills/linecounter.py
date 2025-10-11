#line counter1
def lineCounter(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)
    
#line counter2
#inefficient for large files since it parses each line into .readlines()
def lineCounter(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())