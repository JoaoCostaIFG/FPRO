#!/usr/bin/env python

def raise_exception(alist, value):
    excepts = []
    for i in alist:
        try:
            if i <= value:
                raise ValueError("%d is not greater than %d" % (i, value))
        except ValueError as e:
            excepts.append(e)
    return excepts
