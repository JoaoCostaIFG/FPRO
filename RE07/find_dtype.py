def find_dtype(atuple, data_type):
    vec = []
    comp_str = "<class '" + data_type + "'>"
    for i in atuple:
        if str(type(i)) == comp_str:
            vec.append(i)
    return tuple(vec)
