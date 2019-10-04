n1 = int(input())
n2_temp = n2 = int(input())
skips = 0
while n2_temp > 0:
    n2_temp = n2_temp // 10
    skips += 1

for _ in range(skips):
    n1 = n1 * 10

result = n1 + n2
print(result)
