from datetime import date

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

def calculate_centenary_year(age, current_year):
    return current_year - age + 100

def main():
    name = input("Type your name: ")
    age = int(input("Type your age: "))
    centenary = calculate_centenary_year(age, date.today().year)

    message = "Hello {name}! You will have 100 years in {year}".format(name=name, year=centenary)
    print(message)

main()
