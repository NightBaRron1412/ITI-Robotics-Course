vowels = ("a", "e", "i", "o", "u")

char = input("Enter a charcter: ")

if (char in vowels):
    print(char, "is a vowel")
else:
    print(char, "is not a vowel")