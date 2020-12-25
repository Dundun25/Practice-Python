#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#1. If the number is a multiple of 4, print out a different message.
#2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print("Can your number divided evenly?")
#ask user a number and divider number
num = input("Input a number: ")
divide = int(input("divided by : "))
#Check if their number can be divided evenly or not
if int(num)%divide == 0:
    if int(num)%4 == 0:
        print("It's even number and your number can be divided with 4")
    else:
        print("It's devided evenly")
elif int(num)%4 == 0:
	print("It's not divided evenly but is a multiple of 4")
else:
    print("It's not devided evenly")