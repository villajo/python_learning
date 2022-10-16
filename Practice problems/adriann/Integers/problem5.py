#!/bin/python3

#Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

def main():
    multiples = []
    number = input("Enter a number")
    for num in range(int(number)):
        if int(num) % 3 == 0:
            multiples.append(num)
        elif int(num) % 5 == 0:
            multiples.append(num)
        else:
            continue

    print(multiples)

if __name__ == "__main__":
    main()