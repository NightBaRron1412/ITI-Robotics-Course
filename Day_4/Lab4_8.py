arr_input = [int(n) for n in input(
    "Enter you array integers separated by spaces: ").split()]

print("The second highest number in the entered array is",
      sorted(set(arr_input))[-2])
