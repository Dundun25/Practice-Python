#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function.

def first_n_last(given_list):
	 x = [given_list[0], given_list[-1]]
	 return x


a = [5, 10, 15, 20, 25]
print(first_n_last(a))