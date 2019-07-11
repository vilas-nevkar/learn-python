# Reading csv file
import csv

file_loc = '/media/capricorn/Home1/Master/Code/Python/Core/learn_python/resource/students.csv'
csv_file = open(file_loc, 'r')
csv_reader = csv.reader(csv_file)
for row in csv_reader:
    print(row)
