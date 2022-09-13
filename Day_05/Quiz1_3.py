def is_valid(card_num):
    valid = True

    if (card_num[4] == "-" and card_num[9] == "-" and card_num[14] == "-" and len(card_num) == 19):
        card_num = card_num.split("-")
        card_num = "".join(card_num)

    if (card_num[0] not in "456"):
        valid = False

    elif (len(card_num) != 16):
        valid = False

    elif (not card_num.isdigit()):
        valid = False

    else:
        counter = 1
        for i in range(1, 16):
            if card_num[i] == card_num[i - 1]:
                counter += 1

            else:
                counter = 1

            if counter >= 4:
                valid = False
                break

    if (valid):
        print("Valid")
    else:
        print("Invalid")


N = int(input("How many credit cards do you want to check?: "))

for _ in range(N):
    card_num = input("Enter you credit card number: ")
    is_valid(card_num)
