def translate(astring, table):
    result = ""
    for i in astring:
        flag = False
        for j in table:
            if i == j[0]:
                result += str(j[1])
                flag = True
                break
        if not flag:
            result += i

    return result
