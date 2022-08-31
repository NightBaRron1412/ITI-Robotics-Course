from datetime import date

current_year = date.today().year

birth_year = int(input("Please enter your birth year: "))

print(f"You are {current_year - birth_year} Years Old")