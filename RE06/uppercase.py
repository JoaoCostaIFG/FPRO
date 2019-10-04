def uppercase(astring):
    flag = False
    for i in range(3):
        if astring[i].upper() == astring[i] and astring[i].isalpha():
            flag = True
            break
    if flag:
        astring = astring.upper()
    return astring
