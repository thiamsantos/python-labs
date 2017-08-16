"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

from odd_even import is_odd

def get_even_list(original_list):
    return [i for i in original_list if not is_odd(i)]

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = get_even_list(a)

    print(even_list)

if __name__ == "__main__":
    main()
