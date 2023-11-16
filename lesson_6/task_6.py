# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def custom_sort(requested_list: list):
    odd_list = list(filter(lambda x: x % 2, requested_list))
    even_list = list(filter(lambda x: not x % 2, requested_list))
    even_list.extend(odd_list)
    return even_list
