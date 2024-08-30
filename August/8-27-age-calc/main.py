birth_year = ""
current_year = ""

while not birth_year.isdecimal():
    birth_year = input("Enter your birth year: ")

while not current_year.isdecimal():
    current_year = input("Enter the current year: ")

birth_year = int(birth_year)
current_year = int(current_year)

age = current_year - birth_year

print(f"You are {age} years old.")