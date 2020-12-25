#Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order. 
#For example, say I type the string:

  #My name is Michele
#Then I would see the string:

  #Michele is name My
#shown back to me.


def uno_reverse_card(words):
	word = words.split()#split the given strings
	word = word[::-1]#reverse the order
	reverse = ""#holder variable
	for i in word:#loop the list and store it in holder
		reverse += f"{i} "
	return reverse


#asking input
x = input("Give me text :")
print(uno_reverse_card(x))
