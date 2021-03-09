# Write a password generator in Python. 
# Be creative with how you generate passwords
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# weak(1-3)  = "lower and upper letter"
# moderate(4-6) = weak + numbers
# strong(7-10) = moderate + symbols

import random
import string


def pass_generator(length, security_level, user_id):
    # library
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    letters = lower_case + upper_case
    symbols = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
    symbols = list(symbols)
    # output holder
    generated_password = ""

    # generating password
    if security_level == 1:  # using lower and upper letters
        weak = [random.choice(letters) for i in range(length)]
        for i in weak:
            generated_password += i

    elif security_level == 2:  # using all letters upper and lower and numbers
        choices = ["letter", "number"]
        for i in range(length):
            choice = random.choice(choices)
            if choice == "letter":
                generated_password += random.choice(letters)
            elif choice == "number":
                generated_password += str(random.randint(0, 9))

    elif security_level == 3:  # using all letters upper and lower,number, and symbols
        choices = ["letter", "number", "symbol"]
        for i in range(length):
            choice = random.choice(choices)
            if choice == "letter":
                generated_password += random.choice(letters)
            elif choice == "number":
                generated_password += str(random.randint(0, 9))
            elif choice == "symbol":
                generated_password += random.choice(symbols)
    id_and_pass = f"id : {user_id}\npass : {generated_password}\n\n"
    with open("password.txt", "a+") as text:
        text.write(id_and_pass)
    print(f"your password : {generated_password}")
    print("Your password and id will be saved in password.txt")


# ask length from user
print("Random Password Generator")
while True:
    try:
        user = int(input("Length of your password : "))
        if user > 0:
            break
        print("Must more than 0")
    except ValueError:
        print("Please insert numbers")

# ask security level from user
while True:
    try:
        security = int(input("select security level(1-3): "))
        if 1 <= security <= 3:
            break
        print("Enter number 1-3 only")
    except ValueError:
        print("Whoops you must enter a number")

# ask user id
user_id = input("Your pass name/id (ex : my_id(facebook.com) \n")

# run
pass_generator(user, security, user_id)
