# 22. Program to return the minimum and maximum values in a list of numbers
numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
minimum = min(numbers)
maximum = max(numbers)
print(f"The minimum value in the list is {minimum}")
print(f"The maximum value in the list is {maximum}")
