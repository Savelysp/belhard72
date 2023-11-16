# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
original_list = [1, 2, 3, 4, 5, 6, 7]
def list_reverse(requested_list: list):
    for i in range(len(requested_list)):
        requested_list.insert(i, requested_list.pop())
    return requested_list
# надеюсь тут я тоже не нарушил правил условия
