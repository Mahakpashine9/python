number = int(input("Enter the number : "))
sum_digit = 0

while number > 0:
    digit = number % 10
    sum_digit += digit
    number = number // 10

print(f"Sum of digit: {sum_digit}")