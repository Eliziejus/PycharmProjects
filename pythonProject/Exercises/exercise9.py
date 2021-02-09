import random

user_number = int(input("white any number 1 of 9 "))
un = user_number

n = random.randint(1,9)
if un == n:
    print("You right!")
elif un < n:
    print("You guessed too high")
elif un > n:
    print("You guessed to low")
