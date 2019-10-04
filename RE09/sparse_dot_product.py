def sparse_dot_product(dict1, dict2):
    result = 0
    for i in dict1:
        if i in dict2:
            result += dict1[i] * dict2[i]
    return result
