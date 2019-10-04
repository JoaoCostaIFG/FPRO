side_1 = int(input())
side_2 = int(input())
side_3 = int(input())
max_side = -1
sum_2_side = 0
if side_1 > max_side:
    max_side = side_1
    sum_2_side = side_2 + side_3
if side_2 > max_side:
    max_side = side_2
    sum_2_side = side_1 + side_3
if side_3 > max_side:
    max_side = side_3
    sum_2_side = side_1 + side_2

if sum_2_side <= max_side:
    result = "Not a triangle"
else:
    result = "Scalene"
    if side_1 == side_2 and side_2 == side_3:
        result = "Equilateral"
    else:
        if side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
            result = "Isosceles"

print(result)
