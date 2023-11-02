# Пользователь вводит 3 числа, сказать сколько из них положительных, и сколько отрицательных
user_number1 = input('введите первое число: ')
user_number2 = input('введите первое число: ')
user_number3 = input('введите первое число: ')
negative = int(int(user_number1) < 0) + int(int(user_number2) < 0) + int(int(user_number3) < 0)
positive = int(int(user_number1) > 0) + int(int(user_number2) > 0) + int(int(user_number3) > 0)
print('количество отрицательных чисел: {}\nКоличество положительных: {}'.format(negative, positive))
