string_input = input("Enter a string: ")
print("\nThe unique characters in the entered string are:")
for char in string_input:
    if (string_input.lower().count(char) == 1 and char != " "):
        print(char)
