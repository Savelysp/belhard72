# Вывести первые N чисел кратные M и больше K
n = int(input())
m = int(input())
k = int(input())
while n:
    k += 1
    if k % m:
        continue
    n -= 1
    print(k, end=' ')
