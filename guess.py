#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program is a number guessing game

from random import randint


def main():
    # This function is a number guessing game
    random = randint(1, 100000)
    try:
        while True:
            number = input("enter a number: ")
            number = int(number)
            if number == random:
                print("You won!!!")
                break
            elif number > random:
                print("My number is lower than yours")
            elif number < random:
                print("My number is higher than yours")
            else:
                pass  # you should not be here
    except(Exception):
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
