import random

number = random.randint(1,9)
chances=5

while chances>= 0:

    guess = input("Guess Number: ")

    if guess==number:
        print("You Won!")
        break
    else :
        print("Try Again, Chances Left" , chances)
        chances=chances-1

