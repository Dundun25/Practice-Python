#Write a password generator in Python. 
#Be creative with how you generate passwords
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
#The passwords should be random, generating a new password every time the user asks for a new password. 
#Include your run-time code in a main method.

#Extra:

#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

#weak(1-3)  = "lower and upper letter"
#moderate(4-6) = weak + numbers
#strong(7-10) = moderate + symbols

import random
import string

def pass_generator(lenght):
	#ask input
	while True:
		try:
			level = int(input("select security level(1-3): "))
			if 1 <= level <= 3:
				break
			print("Enter number 1-3 only")
		except ValueError:
			print("Whoops you must enter a number")

	#library
	lower_case = string.ascii_lowercase
	upper_case = string.ascii_uppercase
	letters = lower_case + upper_case
	symbols = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
	symbols = list(symbols)
	#output holder
	password = ""
	
	#generating password based on level input from user

	if level == 1:#using lower and upper letters
		weak = [random.choice(letters) for i in range(lenght)]
		for i in weak:
			password += i

	elif level == 2:#using all letters upper and lower and numbers
		choices = ["letter", "number"]
		for i in range(lenght):
			choice = random.choice(choices)
			if choice == "letter":
				password += random.choice(letters)
			elif choice == "number":
				password += str(random.randint(0,9))
		
	elif level == 3:#using all letters upper and lower,number, and symbols
		choices = ["letter", "number","symbol"]
		for i in range(lenght):
			choice = random.choice(choices)
			if choice == "letter":
				password += random.choice(letters)
			elif choice == "number":
				password += str(random.randint(0,9))
			elif choice == "symbol":
				password += random.choice(symbols)
	
	return password


#ask for user input
while True:
	try:
		user = int(input("Lenght of your password : "))
		if user > 0:
			break
		print("Must more than 0")
	except ValueError:
		print("Please insert numbers")
#store password	
password = pass_generator(user)
print(f"your password : {password}")