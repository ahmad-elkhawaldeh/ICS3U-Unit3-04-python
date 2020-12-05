# !/usr/bin/env python3

# created by: Ahmad El-khawaldeh
# created on: Nov 2020
# This program will tell u if your input is possitive or negative

def main():
    # this function checks if the user inputed the right magic number

    # input
    user_number = int(input("enter an integer :"))

    # process/ output
    if user_number > 0:
        print(" the integer is possitive ")
    elif user_number < 0:
        print(" the integer is negative ")
    else:
        print(" the integer is 0 ")


if __name__ == "__main__":
    main()
