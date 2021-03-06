# Exercise 20: Functions and Files
# 20 of 52,

from sys import argv

script, import_file = argv

def print_all(f):
  print(f.read())
  
def rewind(f):
  f.seek(0)
  
def print_a_line(line_count, f):
  print(line_count, f.readline())
  
current_file = open(input.file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#python3.6 ex20.py test.txt
