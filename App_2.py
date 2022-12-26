# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

with open('input_2.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    i = 2
    list = []
    while i <= n:
        if n % i == 0:
            list.append(i)
            n //= i
            i = 2
        else:
            i += 1
print(list)
