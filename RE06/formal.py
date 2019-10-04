def formal(name):
    formal_name = ""
    name_split = name.split()
    formal_name += name_split[-1] + ","
    name_num = len(name_split)
    i = 0
    for word_name in name_split:
        i += 1
        if i == name_num:
            break
        formal_name += " " + word_name[0].upper() + "."
    return formal_name
