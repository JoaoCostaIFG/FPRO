def odd_range(start, stop, step):
    if start % 2 == 0:
        start += 1
    for i in range(start, stop, step * 2):
        yield i