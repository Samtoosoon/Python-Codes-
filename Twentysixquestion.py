# 26. Program to check if a string starts with a given prefix or ends with a given suffix
string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

if string.startswith(prefix):
    print(f"The string starts with '{prefix}'.")
else:
    print(f"The string does not start with '{prefix}'.")

if string.endswith(suffix):
    print(f"The string ends with '{suffix}'.")
else:
    print(f"The string does not end with '{suffix}'.")
