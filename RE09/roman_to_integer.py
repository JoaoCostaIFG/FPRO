def roman_to_integer(astring):
    num = []
    for i in astring:
        if i == "I":
            num.append(1)
        elif i == "V":
            num.append(5)
        elif i == "X":
            num.append(10)
        elif i == "L":
            num.append(50)
        elif i == "C":
            num.append(100)
        elif i == "D":
            num.append(500)
        else:
            num.append(1000)

    result = num[-1]
    for i in range(len(num) - 1):
        if num[i] >= num[i + 1]:
            result += num[i]
        else:
            result -= num[i]
    return result
