#!user/bin/env python3

# Created by: RJ Fromm
# Created on: Oct 2019
# This program is a number guessing game

import random


def main():

    try:
        random_number = random.randint(1, 100+1)

        while True:

            secret_number = int(input("Guess my secret number: "))

            if random_number < secret_number:
                print("The number is lower")
            elif random_number > secret_number:
                print("The number is higher")
            else:
                print("Good job, you guessed random number", (random_number))
                break
    except Exception:
        print("Enter a real number")


if __name__ == "__main__":
    main()
