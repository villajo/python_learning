#!/bin/python


'''Write a function on_all that applies a function to every element of a list. 
Use it to print the first twenty perfect squares. 
The perfect squares can be found by multiplying each natural number with itself. 
The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16. 
Twelve for example is not a perfect square because there is no natural number m so that m*m=12. 
(This question is tricky if your programming language makes it difficult to pass functions as arguments.)'''


def on_all(list, value):
    if list == None:
        list = []
    if value == 20:
        return list
    list.append([value*value])
    return on_all(list, value + 1)


def main():
    list = []
    list = on_all(list, 0)
    print(list)
    

if __name__ == "__main__":
    main()