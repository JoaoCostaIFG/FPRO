n = int(input()) + 1
result = ""
for i in range(n):
    if i % 3 == 0 and i % 5 == 0:
        pass
    else:
        if i % 3 == 0:
            result += " Fizz"
        else:
            if i % 5 == 0:
                result += " Buzz"
            else:
                result += " " + str(i)
print(result)
