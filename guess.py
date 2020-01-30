#!/usr/bin/env python3
import random

lives = 3
number = random.randint(1, 10)

guess = int(input(f"I'm thinking of a number from 1 to 10, can you guess it in {lives} tries? "))

while(lives > 1 and guess != number):
    lives -= 1
    stmt = "Bigger!" if guess < number else "Smaller!"
    print(f"{stmt} Try again", end='.. ')
    guess = int(input())

if guess == number:
    print(f"You got it with {lives} tries to spare! Good job")
else:
    print(f"Sorry, the number was {number}. Try again!")

