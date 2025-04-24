mail = input('Input @mail:')

player_name = " ".join(mail.split('@')[0:1]) # Имя игрока из почты, первый элеменет списка, преобразовываем список в строку через join
promocode = player_name[1::2] # Расчет промокода
lenpromocode = len(promocode) # красивыый вывод

player_ships_count = input('Input player_ships_count:') # Количетсво кораблей на акке
player_ship = 'корабл'
count = player_ships_count
if player_ships_count.isdigit():
    lastnumber = player_ships_count [-1]
    match int(lastnumber):
        case 1:
            player_ship += 'ь'
        case 2:
            player_ship += 'я'
        case 3:
            player_ship += 'я'
        case 4:
            player_ship += 'я'
        case _:
            player_ship += 'ей'
else:
    print('Entered player_ships_count is not positive integer')

reward_ships_count = input('Input reward_ships_count:') # Количество кораблей для награды
reward_ship = 'корабл'
if reward_ships_count.isdigit():
    lastnumber2= reward_ships_count[-1]
    match int(lastnumber2):
        case 1:
            reward_ship += 'ь'
        case 2:
            reward_ship += 'я'
        case 3:
            reward_ship += 'я'
        case 4:
            reward_ship += 'я'
        case _:
            reward_ship += 'ей'
else:
    print('Entered reward_ships_count is not positive integer')


title = (f'Send to:{mail} Уважаемый игрок Мира кораблей, {player_name}!')

body = (f' Спасибо, что любите и играете в нашу игру. \
        \n Мы заметили, что у вас всего {player_ships_count} {player_ship}. \
        \n Поэтому, мы дарим вам подарок: {reward_ships_count} {reward_ship}!')


print(title, body, '\n', 'Ваш промокод: ' + '\n' ' +','*' * lenpromocode,'+','\n','|', promocode,'|','\n', '+','*' * lenpromocode,'+')


