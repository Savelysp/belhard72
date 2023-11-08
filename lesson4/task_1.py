# Заполнить список степенями числа 2 (от 2^1 до 2^n)
n_value = input('введите число: ')
my_list = [2**i for i in range(1, int(n_value)+1)]
print(my_list)
