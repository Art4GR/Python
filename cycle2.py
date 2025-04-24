value = int(input("Введите число:"))
lit = "--+"
lit2 = "  |"

for el in range(value + 1):
    print("+" + lit * value)
    while el != value:
        print("|" + lit2 * value)
        break
