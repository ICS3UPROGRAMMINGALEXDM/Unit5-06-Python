#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Rounds a decimal number inputted by the user and rounds it to
# the specified decimal place

# this function rounds the inputted decimal number to the specified decimal
# place. Takes the parameter num using the workaround for passing by reference
def round_decimal(num, place):
    # does a different calculation depending on if the number is negative
    if num[0] >= 0:
        num[0] = num[0] * (10**place)
        num[0] += 0.5
        num[0] = int(num[0])
        num[0] = num[0] / (10**place)
    else:
        num[0] = num[0] * (10**place)
        num[0] -= 0.5
        num[0] = int(num[0])
        num[0] = num[0] / (10**place)


def main():
    # getting user input
    u_num = input("Enter a decimal number: ")
    u_place = input("How many decimal places do you need: ")
    numToRound = []

    try:
        placeint = int(u_place)
        d_num = float(u_num)
        # adding the inputted number to the list/array
        numToRound.append(d_num)

        if placeint >= 0:
            # calling the function
            round_decimal(numToRound, placeint)
            # printing to screen the resulting number
            print("\nYour rounded number is... \n\n{}".format(numToRound[0]))
        else:
            print("Decimal place can't be negative")
    except:
        print("Some of the inputted numbers weren't numbers")


if __name__ == "__main__":
    main()
