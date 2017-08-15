"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

def is_palindrome(word):
    return word[::-1] == word

def main():
    word = input("Type a word: ")

    if is_palindrome(word):
        print("The word {word} is a palindrome!".format(word=word))
    else:
        print("The word {word} is NOT a palindrome!".format(word=word))

main()
