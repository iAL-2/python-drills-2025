def fizzbuzz(n):
    t = []
    for i in range(1,n+1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if i % 7 == 0:
            result += "Boom"
        if result:
            t.append(result)
        else:
            t.append(i)
    return t

assert fizzbuzz(30)[1] == 2
result = (fizzbuzz(40))

assert result[0] == 1
assert result[1] == 2
assert result[2] == "Fizz"
assert result[4] == "Buzz"
assert result[6] == "Boom"
assert result[14] == "FizzBuzz"