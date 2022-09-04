from math import sqrt

num_input = int(input("Enter a number: "))
prime = True

for num in range(2, int(sqrt(num_input))+1):
    if num_input % num == 0:
        print(num_input, "is not prime.")
        prime = False
        break
if (prime == True):
    print(num_input, "is prime.")
