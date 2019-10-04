result = original_num = input()
original_num = original_num_temp = int(original_num)
reverse_num = 0
while original_num_temp > 0:
    digito = original_num_temp % 10
    original_num_temp = original_num_temp // 10
    reverse_num = reverse_num * 10 + digito
if original_num == reverse_num:
    result = result + " is a palindrome"
else:
    result = result + " is not a palindrome"
print(result)
