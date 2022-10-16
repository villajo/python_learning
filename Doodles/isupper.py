#!/bin/python

string_case = "Testing1234"

def main():
    for character in list(string_case):
        if character.isupper():
            print(character)
            


if __name__ == "__main__":
    main()