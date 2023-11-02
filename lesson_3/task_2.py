# Пользователь вводит 3 числа, найти среднее арифметическое с точностью 3
user_numbers = input('введите 3 числа: ')
end_of_first_number = user_numbers.index(' ')
start_of_last_number = user_numbers.rindex(' ') + 1
number_one = int(user_numbers[:end_of_first_number])
number_two = int(user_numbers[end_of_first_number + 1:start_of_last_number - 1])
number_thee = int(user_numbers[start_of_last_number:])
sum_of_nubmers = number_one + number_two + number_thee
print(round(sum_of_nubmers / 3, 3))
