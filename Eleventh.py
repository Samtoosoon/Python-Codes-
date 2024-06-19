# Program to generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence}")
