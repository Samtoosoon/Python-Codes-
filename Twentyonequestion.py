# 21. Program to count the occurrences of a specific element in a list
element = input("Enter the element to count: ")
lst = input("Enter the list elements separated by spaces: ").split()
occurrences = lst.count(element)
print(f"The element '{element}' occurs {occurrences} times in the list.")
