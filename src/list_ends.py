"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""

def get_list_start_end(initial_list):
    return [initial_list[0], initial_list[-1]]

def main():
    a = [5, 10, 15, 20, 25]
    print(get_list_start_end(a))

if __name__ == "__main__":
    main()
