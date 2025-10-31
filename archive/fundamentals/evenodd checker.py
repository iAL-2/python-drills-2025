for i in range(1,10):
    if i % 2 == 0:
        print (i, "= even")
    else:
        print (i, "= odd")


n = 7

if n % 2 == 0:
    print (n, "is even")
else:
    print (n, "is odd")

while True:
    try:
        x = int(input("enter a number: "))
        if x % 2 == 0:
            print(x, "= even")
        else:
            print(x, "= odd")

    except ValueError:
        print("Please enter a valid number")
        break