n = int(input("Please Enter any Number: "))

_sum = 0
avg = 0

for i in range(1, n + 1):
    _sum += i
    
avg = _sum / n

print(f"The Sum of Natural Numbers from 1 to 50 = {_sum}")
print(f"Average of Natural Numbers from 1 to 50 = {avg}")