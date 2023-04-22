# Prompting and Passing 

from sys import argv

script, user_name = argv

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(promp)

print(f"""
Alright, so you said {likes} about liking me. 
You livei n {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")



