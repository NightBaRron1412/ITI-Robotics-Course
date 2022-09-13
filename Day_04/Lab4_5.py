num_input = input("Enter a binary number: ")
binary = True
for digit in num_input:
    if digit not in "10":
        print(num_input, "is not binary")
        binary = False
        break

if (binary == True):
    print(num_input, "is binary")
