
import random
print("number geussing game")
number=random.randint(1,9)
chances = 0
print("Guess a number(between 1 and 9):" )

while chances < 5 :

    guess=int(input("enter your guess:-"))


    if guess == number :
        print("Congratuation YOU WON!!!")
        break

    elif guess < number:
        print("your guess was too low: guess a number higher than",guess)

    else:
        print("your guess was too high: guess a number lower than",guess)

    chances += 1

if not chances < 5:
    print("YOU LOSE !!! the number is :",number)
    