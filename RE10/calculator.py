def calculator(expr):
    if type(expr) is int:
        return expr
    temp = ""
    for i in expr:
        if type(i) is tuple:
            temp += str(calculator(i))
        else:
            temp += str(i)
    
    return eval(temp)
