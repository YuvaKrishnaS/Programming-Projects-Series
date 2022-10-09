import random

userWins = 0
compWins = 0

pos = ["rock", "paper", "scissors"]

while True:

    userPick = input("Type (Rock / Paper / Scissors or Q to Quit) : ").lower()

    if userPick == "q":
        break

    elif userPick not in pos:
        continue

    randomNum = random.randint(0,2)
    # 1 - rock , 2 - paper , 3 - scissros
    comPick = pos[randomNum]
    
    if userPick == "rock" and comPick == "scissors":
        userWins += 1

    elif userPick == "paper" and comPick == "rock":
        userWins += 1

    elif userPick == "scissors" and comPick == "paper":
        userWins += 1

    else:
        print("You Lost!")
        compWins += 1

print("You won ", userWins, " times")
print("Computer won ", compWins, " times")
if userWins < compWins:
    print("You Lost")

elif userWins > compWins:
    print("You Won")

else:
    print("Tie!!")