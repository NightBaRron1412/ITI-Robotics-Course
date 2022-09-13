base = int(input("Enter base value: "))
power = int(input("Enter power value: "))

for _ in range(power - 1):
    base = base * base

print("\nThe result is", base)
