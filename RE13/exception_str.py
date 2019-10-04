#!/usr/bin/env python

def exception_str(f):
    try:
        f()
    except Exception as e:
        return str(e)
    return "No exception was raised"
