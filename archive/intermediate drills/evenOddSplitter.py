def evenOddSplitter():
    evens = []
    odds = []

    for i in range(1,101):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print(f"Sum of evens is {sum(evens)}")
    print(f"Sum of odds is {sum(odds)}")

def evenOddSplitter():
    evenSum = 0
    oddSum = 0

    for i in range(1, 101):
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i