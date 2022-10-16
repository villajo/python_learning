#!/bin/python3

#
# Write a function that checks whether an element occurs in a list.
#

def main():
    string_to_check = input("What string would you like to check:")
    substring = input("What substring would you like to check?:")

    split_string = string_to_check.split(" ")
    print(split_string)

    for string in split_string:
        if (string == substring):
            print("Found {0} in testing string".format(substring))

if __name__ == "__main__":
    main()