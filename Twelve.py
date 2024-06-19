# 12. Program to calculate the sum of the digits of a number
num = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in num)
print(f"The sum of the digits of {num} is {sum_of_digits}")
