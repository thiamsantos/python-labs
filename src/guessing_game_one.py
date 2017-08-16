"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

from random import randint

def main():
    wanna_quit = 'n'
    guesses = 0
    number = randint(1, 9)
    print(number)

    while wanna_quit != 'y':
        guess = int(input("Guess a number: "))
        guesses += 1
        if guess > number:
            print("{guess} is too high!".format(guess=guess))
        elif guess < number:
            print("{guess} is too low!".format(guess=guess))
        else:
            print("{guess} is exactly right!".format(guess=guess))

        wanna_quit = input("Do you wanna quit? [y/n]")

    print("You guessed {guesses} times!".format(guesses=guesses))


if __name__ == "__main__":
    main()
