def rm_letter_rev(l, astr):
    temp_str = ""
    for i in range(len(astr) - 1, -1, -1):
        if astr[i] != l:
            temp_str += astr[i]
    return temp_str
