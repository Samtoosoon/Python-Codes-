# 19. Program to remove all punctuation from a string
import string

user_input = input("Enter a string: ")
clean_string = user_input.translate(str.maketrans('', '', string.punctuation))
print(f"The string without punctuation is: {clean_string}")
