#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.


#using set function to get non-duplicated(unique)
def unique_list_set(given_list):
	return list(set(given_list))


#using for loop to get non-duplicated(unique)
def unique_list(given_list):
	unique = []
	for_loop = [unique.append(i) for i in given_list if i not in unique]
	return unique


example_list = [1,2,3,3,3,3,1,1,1,2,2,4,5,1,2,3,1,1,23,121,23,12,312,3123,123,1]
x = unique_list_set(example_list)
y = unique_list(example_list)
print(f"Using set : {x}\nUsing Loop : {y}")
