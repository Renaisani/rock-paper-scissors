import random

###### Game Start! ########
print("Let's play Rock, Paper, Scissors!(Please type rock, paper, or scissors)")

######## Gets user's pick or asks again for a valid pick #########
while True:
    user_pick = input(">").lower()
    if user_pick == "rock":
        break
    elif user_pick == "paper":
        break
    elif user_pick == "scissors":
        break
    else:
        print("Yea that's not a valid input. Do it right this time. or else..")

####### Sets the random number to a computer pick ##########
random_num = random.randint(0, 2) #generates random whole number between 0 and 2
comp_pick = ""
if random_num == 0:
    comp_pick = "rock"
elif random_num == 1:
    comp_pick = "paper"
elif random_num == 2:
    comp_pick = "scissors"

####### Compares user pick and computer pick #########
if comp_pick == "rock":
    if user_pick == "rock":
        print("It's a draw")
    elif user_pick == "paper":
        print("You win!")
    elif user_pick == "scissors":
        print("You lose..")
elif comp_pick == "paper":
    if user_pick == "rock":
        print("You lose..")
    elif user_pick == "paper":
        print("It's a draw")
    elif user_pick == "scissors":
        print("You win!")
elif comp_pick == "scissors":
    if user_pick == "rock":
        print("You win!")
    elif user_pick == "paper":
        print("You lose..")
    elif user_pick == "scissors":
        print("It's a draw")