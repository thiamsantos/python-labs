import string
import random

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation

    return ''.join([random.choice(chars) for i in range(0, 15)])

def main():
    print(generate_password())

if __name__ == '__main__':
    main()
