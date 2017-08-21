def element_search(elements, search):
    for element in elements:
        if element == search:
            return True

    return False

def main():
    print(element_search(range(0, 200), 4))

if __name__ == '__main__':
    main()
