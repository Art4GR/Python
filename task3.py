ship = 'корабл'
count = input('Input ships number: ')
if count.isdigit():
    lastnumber = count[-1]
    match int(lastnumber):
        case 1:
            ship += 'ь'
        case 2:
            ship += 'я'
        case 3:
            ship += 'я'
        case 4:
            ship += 'я'
        case _:
            ship += 'ей'
    print('Answer:', count + ' ' + ship)
else:
    print('Entered value is not positive integer')