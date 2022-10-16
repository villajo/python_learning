#!/bin/python

#Write a program that prints a multiplication table for numbers up to 12

def main():

    for i in range(1,12):
        for j in range(1,12):
            print("{0} x {1} = {2}".format(i,j,i*j))


if __name__ == "__main__":
    main()