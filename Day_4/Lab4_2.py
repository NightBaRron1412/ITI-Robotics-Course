from math import sqrt

def is_prime(n):
    for num in range(2, int(sqrt(n))+1):
        if n % num == 0:
            return False
            break
        
    return True

start = int(input("Enter start value: "))
end   = int(input("Enter end value: "))

for num in [n for n in range(start, end + 1) if (is_prime(n) == True)]:
    print(num)