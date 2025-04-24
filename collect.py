employees = {
    'Иванов': {
        'Иван': [81117776654, 81117776655],
        'Петр': [81117776656],
        'Сергей': [81117776658]
    },
    'Петров': {
        'Иван': [81117776644],
        'Петр': [81117776646, 81117776647],
        'Сергей': [81117776648]
    },
    'Сергеев': {
        'Иван': [81117776634],
        'Петр': [81117776636],
        'Сергей': [81117776638, 81117776639]
    }
}

surname, name, tel = input('Введите Фамилию, Имя, Телефон через пробел:').split(' ')
tel = int(tel)
if surname in employees.keys():
    if tel in employees[surname][name]:
        message = (f'Телефон {tel} пользователя {surname} {name} уже есть в базе. Телефоны сотрудника: {employees[surname][name]}')
    else:
        employees[surname][name] += [tel]
        message = (f'Телефон {tel} пользователя {surname} {name} записан в базу. Телефоны сотрудника: {employees[surname][name]}')
else:
    message = (f'Пользователь {surname} {name} не найден в базе.')



if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    pattern = r'Пользователь ([\s\S]+) ([\s\S]+) не найден в базе.' if message.startswith('Пользователь') \
        else r'Телефон ([\s\S]+) пользователя ([\s\S]+) ([\s\S]+) уже есть в базе. Телефоны сотрудника: ([\s\S]+)' if 'уже есть' in message \
        else r'Телефон ([\s\S]+) пользователя ([\s\S]+) ([\s\S]+) записан в базу. Телефоны сотрудника: ([\s\S]+)'
    import re

    match = re.findall(pattern, message)
    assert match, 'Проверь корректность сообщения.'
    if not message.startswith('Пользователь'):
        telephone_number, first_name, second_name, _ = match[0]
        telephone_numbers = employees.get(first_name, {}).get(second_name)
        assert telephone_numbers, f'Для сотрудника {first_name} {second_name} не удалось получить информацию по телефонным номерам.'
        assert not [item for item in telephone_numbers if not isinstance(item,
                                                                         int)], f'Все телефонные номера должны иметь тип int. Текущией список телефонов: {telephone_numbers}'
        assert len(set(telephone_numbers)) == len(
            telephone_numbers), f'В списпе телефонов есть повторения. Проверь, чтобы этого не было. Текущий список телефонов: {telephone_numbers}'

    # вывод в терминал результата
    print(message)


