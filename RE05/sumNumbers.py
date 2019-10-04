def sum_numbers(n):
    total_sum = 0
    for i in range(1, int(n) + 1):
        total_sum += i
    return total_sum


n = input()
print(sum_numbers(n))
