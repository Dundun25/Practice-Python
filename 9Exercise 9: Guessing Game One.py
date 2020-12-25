#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
#then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the 
#user input lessons from the very first exercise)
#Extras:
#Keep the game going until the user types 
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

print("This is a guessing game")
while True:
    game = 0
    wrong_guess = 0
    right = False
    num = random.randint(1,9)
    while right == False:
        guess = input("Guess a number(1-9): ")
        try:
            guess = int(guess)
        except:
            print("Wrong Input")
            break
        game += 1
        if num == int(guess):
            print("Your guess is right!")
            right = True
        elif guess < num:
            print("too low!")
            wrong_guess += 1
        elif guess > num:
            print("too high!")
            wrong_guess += 1
        else:
            print("wrong input")
    print(f"""
    {wrong_guess} times wrong guess,
    type (exit) to exit the game or (play) to replay
    """)
    again = input("> ")
    if again.lower() == "exit":
        print("Thanks for playing")
        break
    elif again.lower() == "play":
        continue
    else:
        print("wrong input I guess you wanna play again")