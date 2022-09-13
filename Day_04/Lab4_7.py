string_input = input("Enter a string: ")
counter = 0

for char in string_input.lower():
    if char in "aeiou":
        counter += 1

print(f'"{string_input}" contains {counter} vowels')
