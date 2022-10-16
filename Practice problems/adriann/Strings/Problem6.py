#!/bin/python3

#Print palendromic numbers


def main():
    for number in range(1,10000):
        num_list = list(str(number))
        if number == int("".join(reversed(num_list))):
            print("{} is a palendrome.".format(number))

if __name__ == "__main__":
    main()