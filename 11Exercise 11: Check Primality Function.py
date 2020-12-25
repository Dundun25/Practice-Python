#Ask the user for a number and determine whether the number is prime or not.
#(For those who have forgotten, a prime number is a number that has no divisors.). 
#You can (and should!) use your answer to Exercise 4 to help you.
#Take this opportunity to practice using functions, described below.

#you must to make a def function 
#for more information visit : https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html


def prime(num):
	if_false = "Your Number is not Prime Number"
	if_true = "Your Number is Prime Number"
	divisors = [div for div in range(1,num-1) if num%div == 0]
	print("divided by : ", divisors)
	if divisors == ([1] or []):
		return if_true
	else:
		return if_false


ask_number = int(input("Give a Number : "))
print(prime(ask_number))