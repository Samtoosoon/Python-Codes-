# 14. Program to read multiple lines of input and print them
print("Enter lines of text (enter an empty line to finish):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("You entered:")
for line in lines:
    print(line)
