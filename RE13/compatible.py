#!/usr/bin/env python

def compatible(A, B):
    # assert len(A[0]) == len(B), "A and B cannot be multiplied"
    if len(A[0]) != len(B):
        return AssertionError('A and B cannot be multiplied',)
    return "A and B can be multiplied"
