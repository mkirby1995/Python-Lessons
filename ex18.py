#this one is like your scripts with argv
def print_two(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")
  
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")
  
#this jsut takes one argument
def print_one(arg1):
  print(f"arg1: {arg1}")
  
#this takes no arguments
def print_none():

print_two("Matt", "Kirby")
print_two_again("Matt", "Kirby")
print_one("First!")
print_none()

python3.6 ex18.py
