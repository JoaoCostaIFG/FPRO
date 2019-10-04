#!/usr/bin/env python

def count_exceptions(f, n1, n2):
    count = 0
    for i in range(n1, n2 + 1):
        try:
            f(i)
        except Exception:
            count += 1
    return count
