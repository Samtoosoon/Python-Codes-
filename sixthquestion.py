# Program to read content from a text file and print it
try:
    with open("output.txt", "r") as file:
        content = file.read()
        print("Content of the file:")
        print(content)
except FileNotFoundError:
    print("File not found.")
