# Дан словарь, ключ - Название страны, значение - список городов, на вход поступает город,
# необходимо сказать из какой он страны
city_dict = {'Belarus': ['Minsk', 'Grodno', 'Mogilev'],
             'Russia': ['Moscow', 'St.Petersburg', 'Ryazan'],
             'Ukraine': ['Kiev', 'Odessa', 'Bakhmut']}


def country_finder(requested_data: dict, city: str):
    for i in requested_data.keys():
        country = i
        for j in requested_data[i]:
            if j == city:
                return country


print(country_finder(city_dict, 'Mogilev'))
