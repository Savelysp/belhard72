# Сделать калькулятор: у пользователя спрашивается число,
# потом действие и второе число
while True:
    first_number = int(input())
    action = input()
    second_number = int(input())
    if action == "+":
        print(first_number + second_number)
    elif action == "-":
        print(first_number - second_number)
    elif action == "*":
        print(first_number * second_number)
    elif action == "/":
        print(first_number / second_number)
    else:
        break
