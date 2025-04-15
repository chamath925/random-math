import random
options = ["rock","paper","scissors"]
user_choice = input("Chose rock peper or scicssors: ")
computer_choice = random.choice(options)
print("you chose",user_choice)
print("computer chose",computer_choice)

if user_choice == computer_choice:
    print("it's a tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("rock smash the scissors, you win")
elif user_choice == "paper" and computer_choice == "rock":
    print("paper covers the rock, you win")    
elif user_choice == "scissors" and computer_choice == "paper":
    print("scissors cut the paper, you win")
else:
    print("you lose")