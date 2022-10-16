#!/bin/python

#Write a function that computes the running total of a list.

def main():
    running_total = []
    final_total = 0
    for _ in iter(int, 1):
        value = input("Enter a number to be added to running total:")
        print(value)
        if len(value) == 0:
            break
        running_total.append(value)
    
    for number in running_total:
        final_total = int(number) + final_total
    
    print(final_total)
if __name__ == "__main__":
    main()