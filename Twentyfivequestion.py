# 25. Program to copy contents of one text file to another
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Contents of {source_file} have been copied to {destination_file}.")
except FileNotFoundError:
    print("Source file not found.")
