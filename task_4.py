# Пользователь вводит 3 числа, сказать сколько из них положительных, и сколько отрицательных
user_numbers = input('введите 3 числа: ')
negative_numbers = user_numbers.count('-')
positive_numbers = 3 - int(negative_numbers)
print('количество отрицательных чисел: {}\nКоличество положительных: {}'.format(negative_numbers, positive_numbers))
