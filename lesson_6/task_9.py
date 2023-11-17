# Дан словарь словарей, ключ внешнего словаря - id пользователя,
# значение - словарь с данными о пользователе (имя, фамилия, телефон, почта),
# вывести имена тех, у кого не указана почта (нет ключа email или значение этого ключа - пустая строка)
users_data = {'id83085': {'name': 'Misha', 'second name': '', 'phone': '', 'email': ''},
              'id9125': {'name': 'Masha', 'second name': '', 'phone': '', 'email': 'masha@gmail.com'},
              'id291845': {'name': 'Vlad', 'second name': '', 'phone': ''},
              'id19284': {'name': 'Lena', 'second name': '', 'phone': '', 'email': ''}}


def email_check(users_data: dict):
    names = []
    for i in users_data.values():
        if not i.setdefault('email'):
            i['email'] = None
        for j in i.items():
            if j[0] == 'email' and not j[1]:
                names.append(i['name'])
    return names


print(email_check(users_data))
