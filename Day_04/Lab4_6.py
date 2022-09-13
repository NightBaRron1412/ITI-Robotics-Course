string_input = input("Enter a string: ")
char_input = input("Enter a char to remove: ")

print(
    "".join([char for char in string_input if char.lower() != char_input.lower()]))
