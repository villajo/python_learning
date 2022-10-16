#!/bin/python

#Write a guessing game where the user has to guess a secret number. After every guess the program tells the 
# user whether their number was too large or too small. At the end the number of tries needed should be printed. 
# It counts only as one try if they input the same number multiple times consecutively.

import random


def main():
    secret_value = random.randint(1,100)
    found = False
    tries = 1
    print(secret_value)

    for _ in iter(int, 1):
        value = int(input("Guess the number:"))
        if value == secret_value:     
            if tries > 1:
                print("You found it! in {0} tries!".format(tries))    
            elif tries == 1:
                print("You found it on the first try!")
            break
        else:
            tries = tries + 1
            print("Nope.. Try again!")
            if value < secret_value:
                print("Go higher")
            elif value > secret_value: 
                print("Go lower")

    


if __name__ == "__main__":
    main()