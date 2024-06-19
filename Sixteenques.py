# 16. Program to count the frequency of each character in a string
from collections import Counter

user_input = input("Enter a string: ")
frequency = Counter(user_input)
print("Character frequency:")
for char, freq in frequency.items():
    print(f"{char}: {freq}")
