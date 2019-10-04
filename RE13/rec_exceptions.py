#!/usr/bin/env python

def rec_exceptions(l):
    excepts = []
    if type(l) is list:
        for i in l:
            excepts += rec_exceptions(i)
    else:
        try:
            for i in l():
                excepts += rec_exceptions(i)
        except Exception:
                try:
                    l()
                except Exception as e:
                    excepts.append(e)
    return excepts
