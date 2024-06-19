# Program to check if a substring is present in a string
string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in string:
    print(f"The substring '{substring}' is present in the string.")
else:
    print(f"The substring '{substring}' is not present in the string.")
