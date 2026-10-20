# to generate random number
import random

jackpot =random.randint(1, 100)
guess = int(input("Chal guess kar"))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")

    guess = int(input("Chal guess kar"))
    counter += 1

print("Sahi jawab")
print("You took", counter, "attempts")