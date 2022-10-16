#!/bin/python3

#Leap years.. Write a program that prints the next 20 leap years.


def main():
    starting_year = int(2000)
    leap_count = int(0)
    year_offset = int(0)

    while leap_count < 20:

        if (starting_year + year_offset) % 4 == 0 and str(starting_year + year_offset)[-2:] != "00":
            print("{} is a leap year..".format(starting_year + year_offset))
        if str(starting_year + year_offset)[-2:] == "00" and (starting_year + year_offset) % 400 == 0:
            print("{} is a leap year..".format(starting_year + year_offset))
        if year_offset == 20:
            break

        year_offset = year_offset + 1

if __name__ == "__main__":
    main()