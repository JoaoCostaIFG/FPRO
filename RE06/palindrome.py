def palindrome(astring):
    counter = 0
    pali_max_len = len(astring)
    for i in range(2, pali_max_len + 1):
        for j in range(0, pali_max_len - i + 1):
            temp_str = ""
            for k in range(j, j + i):
                temp_str += astring[k]
            if temp_str == temp_str[::-1]:
                counter += 1
    result = "For string '{}': {} palindrome substrings".format(astring, counter)
    return result
