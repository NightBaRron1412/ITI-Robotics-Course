list_input = [int(n) for n in input(
    "Enter you list items separated by spaces: ").split()]

occurrence = [list_input.count(i) for i in list_input]

highest_freq = list_input[occurrence.index(max(occurrence))]

print("\nThe highest frequency element in the list is", highest_freq)
