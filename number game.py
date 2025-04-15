import random
playing = True
number = str(random.randint(10,20))
print("I'll genarate numbers from 10,20 ,you have to guess the number")
print("The game will end when you get a one hero")
while playing:
    guess = input("give me your best guess: ")

    if number == guess:
        print('you win the game')
        print("the number was",number)
        break

    else:
        print("your guess isn't quite right . try again")