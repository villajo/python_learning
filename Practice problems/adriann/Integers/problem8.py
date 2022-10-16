#!/bin/python

#Check if number is prime or not. 

def is_prime(num):
    for i in range(1,int(num)):
        for j in range(1,int(num)):
            if (i * j) == int(num):
                return False
    return True 


def main():
    number = input("What number do you want to check?:")
    if is_prime(number):
        print("Number is prime")
    else:
        print("Number is not prime")


if __name__ == "__main__":
    main()