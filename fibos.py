'''
# fibos_file = open("fibos_file.txt", "a+")
fibos_dict = {}
fibos_dict[0] = 0
fibos_dict[1] = 1


def fibos(n):
    n = abs(n)
    try:
        return fibos_dict[n]
    except KeyError:
        for i in range(len(fibos_dict), n + 1):
            fibos_dict[i] = fibos_dict[i - 2] + fibos_dict[i - 1]
        return fibos_dict[n]


print(fibos(300000))
'''
from numpy import matrix

def fib(n):
    return (matrix("0 1; 1 1" if n >= 0 else "-1 1; 1 0", object) ** abs(n))[0, 1]


print(fib(600000))
