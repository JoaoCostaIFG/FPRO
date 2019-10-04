n = int(input())
result = True
if n >= 2:
    sqrt_n = int(n ** 0.5)
    for i in range(2, n, 1):
        if n % i == 0:
            result = False
            break
print(result)
