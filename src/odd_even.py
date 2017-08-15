"""Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
"""

def is_odd(number):
    return number % 2 == 1

def main():
    number = int(input("Type a number: "))
    number_is_odd = is_odd(number)

    if number_is_odd:
        print("{number} is odd!".format(number=number))
    else:
        print("{number} is even!".format(number=number))

main()
