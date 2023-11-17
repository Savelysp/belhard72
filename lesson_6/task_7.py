# Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних чисел одним из соседей является число с противоположной стороны списка
random_list = [1, 2, 3, 4, 5, 6]


def calc_sum(requested_list: list):
    for i in range(len(requested_list)):
        yield requested_list[i - 1] + requested_list[i - len(requested_list) + 1]


result = dict(zip(random_list, [i for i in calc_sum(random_list)]))
print(result)
