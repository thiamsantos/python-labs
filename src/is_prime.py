"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
"""

from divisors import get_divisors

def is_prime(number: int) -> bool:
    divisors = get_divisors(number)

    if len(divisors) == 2:
        return True

    return False

def main():
    number = int(input("Type a number: "))
    number_is_prime = is_prime(number)

    if number_is_prime:
        print("{number} is a prime number!".format(number=number))
    else:
        print("{number} is NOT a prime number!".format(number=number))

if __name__ == "__main__":
    main()
