'''We are going to write a program that generates a random number and asks the user to guess it.
If the player's guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user's guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
Hint: Use the random module.'''


import random

n = random.randint(1, 100)
guesses = 0
a = -1

while(a != n):
    guesses += 1
    a = int(input("Guess the Number: "))
    if a > n:
        print("Lower number please.")
    elif a < n:
        print("Higher number please.")

print(f"You have guessed number {n} correctly in {guesses} attempts.")