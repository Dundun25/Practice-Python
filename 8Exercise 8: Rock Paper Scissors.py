#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

import random
count = 0
message = "Play the game?(Y/N)" 
while True:
    print(message)
    play = input()
    if play.lower() == "y":
        count += 1
        message = f"({count})Play the game again?(Y/N)"
        p1 = input("player one choose(R/P/S): ")
        p2 = input("player two choose(R/P/S): ")
        p1,p2 = p1.lower(),p2.lower()
        choice = ["r","p","s"]
        if p1 or p2 not in choice:
            print("Wrong input")
        elif p1 == p2:
            print("Draw bruh..")
        elif (p1 == "r" and p2 == "s") or (p1 == "p" and p2 == "r") or (p1 == "s" and p2 == "p"):
            win =["Player one you are great!","Player one you win!", "Player one you are amazing!","Player one is the sherlock"]
            print(random.choice(win))
        elif (p2 == "r" and p1 == "s") or (p2 == "p" and p1 == "r") or (p2 == "s" and p1 == "p"):
            win =["Player two you are great!","Player two you win!", "Player two you are amazing!","Player two is the sherlock"]
            print(random.choice(win))
    elif play.lower() == "n":
        break
    else:
        print('please type "Y" for play again or "N" to exit')