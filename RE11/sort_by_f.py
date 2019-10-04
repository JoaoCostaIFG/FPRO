def sort_by_f(l):
    return sorted(l, key=lambda i: i if i < 5 else 5 - i)