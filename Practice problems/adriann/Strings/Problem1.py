#!/bin/python3




def main():
    list = ['I', "am", "writing", "this", "to", "test", "longest", "member"]
    longest_word = None

    for string in list: 
        if longest_word == None:
            longest_word = string
        else:
            if len(longest_word) < len(string):
                longest_word = string
    
    print(longest_word)


if __name__ == "__main__":
    main()