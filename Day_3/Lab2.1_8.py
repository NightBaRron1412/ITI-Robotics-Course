print("Enter '0' to stop\n")

_sum = 0
num_counter = 0

while (True):
    user_input = int(input("Enter a number: "))
    
    if (user_input == 0):
        break
    
    else:
        num_counter += 1
        _sum += user_input

print("\nThe sum of all entered numbers is", _sum)
print("The average of all enterd numbers is", _sum / num_counter)