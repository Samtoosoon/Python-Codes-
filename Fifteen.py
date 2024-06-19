# 15. Program to read data from a CSV file and print it
import csv

filename = 'data.csv'
try:
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))
except FileNotFoundError:
    print(f"The file {filename} was not found.")
