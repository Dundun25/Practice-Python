#Take two lists, say for example these two:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#Extras:
#1. Randomly generate two lists to test this
#2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

from random import randint

print("How long list 1 do you want:")
long1 = int(input())
print("How long list 2 do you want:")
long2 = int(input())

print("in range 1-100","Generating 2 random list...", sep="\n")
list1 = [randint(1,100) for i in range(long1)]
list2 = [randint(1,100) for i in range(long2)]
print("List 1:",list1,"List 2:",list2, sep = "\n")
list = list1 + list2
unique=[]
for num in list:
    if num not in unique:
        unique.append(num)
print(f"Get unique number({len(unique)}) :", unique, sep="\n") 