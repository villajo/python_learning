#!/bin/python

list_of_stuff = ['fdksjaflksj','buoinmdoijo','dmoimlidjlh']
global full_string

def main():
    print(list(list_of_stuff))
    full_string = ""
    for record in list_of_stuff:
        full_string = full_string + record

    list_test = list(full_string)
    sorted_string = sorted(list_test, reverse=True)
    print("".join(sorted_string))
    #full_string = list(full_string).sort()

if __name__ == "__main__":
    main()