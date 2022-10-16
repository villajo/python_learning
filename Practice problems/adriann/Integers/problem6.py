#!/bin/python

#Write a program that asks the user for a number n and gives them the possibility to choose between 
#computing the sum and computing the product of 1,…,n.

def compute(num, function):
    value = None
    for num in range(1, int(num)):
        if function == "sum":
            value = num + value
        if function == "product":
            if value == None:
                value = num * 1
            else:
                value = num * value
    return value

def main():
    number = input("Enter a number:")
    option = input("Would you like to compute the sum or the product of this number?:")

    if option == "sum":
        print("The sum of the values is {}".format(compute(number,option)))
    elif option == "product":
        print("The product of the numbers is {}".format(compute(number,option)))
    else:
        print("This is why we do not have nice things..")

if __name__ == "__main__":
    main()