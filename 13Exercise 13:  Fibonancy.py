#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
#is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#define fibonacci function
def fibo(lenght):
	#this is for initiation
	Fibonacci = [1]
	a = 1
	answer = ""
	#if user input less than 1
	if lenght < 1:
		answer = "Null"
	#if user input more than one
	else:
		#loop through to get fibonacci number(number index i + index i+1)
		for i in range(lenght-1):
			Fibonacci.append(a)
			a = Fibonacci[i] + Fibonacci[i+1]
		#turn list into strings
		for i in range(lenght-1):
			answer += f"{Fibonacci[i]}, "
	return answer

#ask user for lenght
ask = int(input("Lenght of Fibonacci sequence: "))
print(fibo(ask))