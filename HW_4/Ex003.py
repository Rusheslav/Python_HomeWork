# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

n = input('Задайте последовательность чисел единой строкой: ')
print([int(i) for i in n.split() if n.count(i) == 1])
