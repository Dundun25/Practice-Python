#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#(Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. 
#(Hint: the string "\n is the same as pressing the ENTER button)

#get input from user
name = input("What is your name? ")
age = input("How old are you? ")
#turn current age to integer
age = int(age)
#find the year user become 100 years old
year = 2020 + 100 - age
message = f"Hi {name} You will be 100 years old at year: {year}"
print(message)

#ask user if they want a copy of the message
confirm = input("do you want copy of last message? (Y/N)")
if confirm == "Y" or "y":
    count = int(input("How Many message? "))
    #when user want only 1 copy
    if count == 1:
        print("Here your message for",str(count),"number of copy :")
        for i in range (count):
            print(message)
    #when user want more than 1 copy
    else:
        print("Here your message for",str(count),"numbers of copy :")
        for i in range (count):
            print(message)
#when user dont want message copy
else:
    print("Thank You!")