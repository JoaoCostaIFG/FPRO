def is_perfect(n):
    div_sum = 0
    max_div = (n // 2) + 1
    for i in range(1, max_div):
        if n % i == 0:
            div_sum += i
    return div_sum == n


n = int(input())
print(is_perfect(n))
