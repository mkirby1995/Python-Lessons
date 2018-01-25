#Exercise 14: Prompting and Passing
# 14 of 52

from sys import argv
script, user_name = argv
prompt = '> '

print(f'Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me{user_name}?")
likes = input(promt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
print(f"""
Alright, so you siad {likes} about likeing me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
