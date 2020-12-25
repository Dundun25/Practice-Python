#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input("give me a number: "))
list =[]
for num in range (1,number+1):
    if number % num == 0:
        list.append(num)
print("Your number divisors are: ")
print(list)