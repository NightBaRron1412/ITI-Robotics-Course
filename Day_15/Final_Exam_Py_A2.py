input_list = []
par = []
impar = []

for _ in range(15):
    input_list.append(int(input("Enter a number: ")))

for num in input_list:
    if (num % 2 == 0):
        par.append(num)
    else:
        impar.append(num)

    if (len(par) == 5):
        for i in range(len(par)):
            print(f"par[{i}] = {par[i]}")
        par = []

    if (len(impar) == 5):
        for i in range(len(impar)):
            print(f"impar[{i}] = {impar[i]}")
        impar = []

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
