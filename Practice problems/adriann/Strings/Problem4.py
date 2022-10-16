#!/bin/python3

#Return elements that occur on odd positions in a list.. 

def main():
  input_string = input("Enter a string:").split(" ")
  i = 1
  for string in input_string:
    if i % 2 == 1:
        print(string)
    i = i + 1

if __name__ == "__main__":
    main()