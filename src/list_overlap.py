"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

from random import randint

def list_overlap(list_a, list_b):
    return [i for i in list(set(list_a)) if i in list_b]

def random_list(length):
    return [randint(0, length) for i in range(length)]

def main():
    list_a = random_list(10)
    list_b = random_list(20)
    overlap = list_overlap(list_a, list_b)

    message = "list_a={list_a}\nlist_b={list_b}\noverlap={overlap}".format(list_a=list_a, list_b=list_b, overlap=overlap)
    print(message)

main()
