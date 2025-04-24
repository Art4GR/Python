first_word = input('Введите слово референс:')
second_word = input('Введите слово игрока:')

if sorted(first_word) == sorted(second_word):
    print ('Матное слово')
else:
    print('Нормальное слово')