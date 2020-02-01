#!/usr/bin/env python3
import random

def promptForInt(s):
    while True:
        try:
            guess = int(input(s))
            return guess
        except ValueError:
            print("You must enter an integer!")

# Setup
## Determine Difficulty
## Easy   --> 5 lives, number ϵ [1,10]
## Med    --> 4 lives, number ϵ [1,30]
## Hard   --> 3 lives, number ϵ [1,50]
## Custom --> Choice lives,  [Choice, Choice]
invalidMode = True
while invalidMode:
    mode = input("Select your difficulty: [Easy, Med, Hard] ").strip().lower()
    if mode in ["easy", "med", "hard",
                "eas", "me", "har",
                "ea", "m", "ha",
                "e", "h",
                "1", "2", "3"
                ]:
        invalidMode = False
    else:
        print(f"{mode.capitalize()} is not a valid difficulty")

likelyEasy = mode == "easy" or mode == "eas" or mode == "ea" or mode == "e" or mode == "1"
likelyMed  = mode == "med" or mode == "me" or mode == "m" or mode == "2"
likelyHard = mode == "hard" or mode == "har" or mode == "ha" or mode == "h" or mode == "3"
lives  =  3 if likelyHard else ( 4 if likelyMed else  5)
upper  = 50 if likelyHard else (30 if likelyMed else 10)
number = random.randint(1, upper)

print(f"I'm thinking of a number from 1 to {upper}. Can you guess it in {lives} tries?")
guess = promptForInt("Your guess.. ")

while(lives > 1 and guess != number):
    lives -= 1
    stmt = "Bigger!" if guess < number else "Smaller!"
    guess = promptForInt(f"{stmt} Try again.. ")

if guess == number:
    lives -= 1
    print(f"You got it with {lives} tries to spare! Good job")
else:
    print(f"Sorry, the number was {number}. Try again!")
