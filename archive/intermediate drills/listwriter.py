def listWriter():
    l = ['apple','banana','strawberry']
    with open("text.txt", "w", newline="", encoding="utf-8") as f:
        for word in l:
            f.write(word + "\n")

    with open("text.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        print(line.strip().upper())
