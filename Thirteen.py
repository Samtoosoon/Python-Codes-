# 13. Program to calculate age based on birth year
from datetime import date

birth_year = int(input("Enter your birth year: "))
current_year = date.today().year
age = current_year - birth_year
print(f"You are {age} years old.")
