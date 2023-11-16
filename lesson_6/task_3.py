# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
def list_shift(requested_list: list, N: int):
    while len(requested_list) - N:
        requested_list.append(requested_list.pop(0))
        N += 1
    return requested_list
