def inner(u, v):
    prod_escalar = 0
    for i in range(len(u)):
        prod_escalar += u[i] * v[i]
    return prod_escalar
