def map_reduce(n1, n2):
    import functools
    return int(functools.reduce(lambda x, y: x * y if x * y < 50 else x + y, [i**2 for i in range(n1, n2) if i % 2 != 0]))