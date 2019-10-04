def aDigits(n1, n2, n3):
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    max_dig = med_dig = min_dig = 0
    if n1 > n2:
        max_dig = n1
        if n2 > n3:
            med_dig = n2
            min_dig = n3
        else:
            med_dig = n3
            min_dig = n2
    else:
        max_dig = n2
        if n1 > n3:
            med_dig = n1
            min_dig = n3
        else:
            med_dig = n3
            min_dig = n1
    if n3 > max_dig:
        max_dig = n3
        if n1 > n2:
            med_dig = n1
            min_dig = n2
        else:
            med_dig = n2
            min_dig = n1
    return (max_dig * 100 + med_dig * 10 + min_dig)


n1 = input()
n2 = input()
n3 = input()
print(aDigits(n1, n2, n3))
