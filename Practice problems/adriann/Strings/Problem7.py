#!/bin/python3

#Write three functions that compute the sum of the numbers in a list: using a for-loop, 
# a while-loop and recursion. (Subject to availability of these constructs in your language of choice.)

def for_loop(list):
    return_val = 0
    for i in list:
        return_val = int(i) + return_val
    return return_val
    
def while_loop(list):
    i = len(list) - 1
    return_val = 0
    while i >= 0:
        return_val = return_val + int(list[i])
        i = i - 1
    return return_val

value = 0

def recursion(list):
    if len(list) == 1:
        return list[0]
    else: 
        number = list[0]
        list.pop(0)
        return number + recursion(list)

def main():
    list = [1,2,5,4,2,67,8,3,7,8]
    print(for_loop(list))
    print(while_loop(list))
    print(recursion(list))

if __name__ == "__main__":
    main()