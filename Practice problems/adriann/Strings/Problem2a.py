#!/bin/python

#Done a different way instead of cheating.. 


def main():
    list = ["I", "Am", "Writing", "This", "To", "Reverse"]
    reverse_list = []

    for element in list:
        temp_list = [element]
        temp_list.extend(reverse_list)
        reverse_list = temp_list

    print(reverse_list)

if __name__ == "__main__":
    main()