def triplet(atuple):
    n = len(atuple)
    flag = False
    for i in range(n):
        if flag:
            break
        flag = False
        for j in range(i + 1, n):
            if flag:
                break
            for k in range(j + 1, n):
                if atuple[i] + atuple[j] + atuple[k] == 0:
                    triplet_sum = (atuple[i], atuple[j], atuple[k])
                    flag = True
    if not flag:
        triplet_sum = ()
    return triplet_sum
