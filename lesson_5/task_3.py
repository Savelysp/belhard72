# Вывести четные числа от 2 до N по 5 в строку

# тут я немного схитрил, так как для того, чтобы было по 5 цифр в строке,
# я пихаю в проверке не итерацию цикла, а само проверяемое число, так как оно по математике будет работать энивей,
# но если захочу сделать не чётные числа, то облом будет

# n = int(input())
# for i in range(2, n):
#     if not i % 2:
#         if i % 5:
#             print(i, end=' ')
#         else:
#             print(i)
#     else:
#         continue

# Этот вариант уже работает для не чётных, но для чётных не работает :/

# n = int(input())
# iteration = 0
# for i in range(2, n):
#     iteration += 1
#     if i % 2:
#         if iteration % 5:
#             print(i, end=' ')
#         else:
#             print(i)
#     else:
#         continue

# бляха, ну я и дурень, решение простое, а долбился минут 20

n = int(input())
iteration = 0
for i in range(2, n):
    iteration += 1
    if not i % 2:
        if iteration % 5:
            print(i, end=' ')
        else:
            print(i)
    else:
        iteration -= 1
        continue
