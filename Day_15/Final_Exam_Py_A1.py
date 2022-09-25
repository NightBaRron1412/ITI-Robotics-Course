input_list = []
for _ in range(10):

    user_input = int(input("Enter a number: "))

    if (user_input <= 0):
        input_list.append(1)
    else:
        input_list.append(user_input)

for i in range(10):

    if (input_list[i] <= 0):
        print(f"X[{i}] = 1")
    else:
        print(f"X[{i}] = {input_list[i]}")
