from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t [randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
        else:
            print("You win", player, "Smashes", player)
    elif player == "Paper":
       if computer == "Scissors":
           print("You lose", computer, "cut", player)
       else:
           print("You win", player, "cover",computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer,"smashes", player)
        else:
            print("You win", player, "cut", computer)
    else:
        print("This is not valid player")
    player = False
    computer = t [randint(0,2)]
