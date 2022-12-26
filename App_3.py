# 3. Задайте последовательность чисел. 
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

with open('input_3.txt', 'r', encoding='utf-8') as file:
    list = file.readline().split()
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print('Исходный список:', list)
    print('Новый список:', new_list)