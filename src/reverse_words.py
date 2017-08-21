def reverse_words(words):
    return ' '.join(words.split(' ')[::-1])

def main():
    print(reverse_words('My name is Michele'))

if __name__ == '__main__':
    main()
