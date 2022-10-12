from random import randint

N = '0'
while not (N.isdigit() and int(N) > 0):
    N = input('Введите натуральное число: ')

N = int(N)

lst = [randint(-N, N) for i in range(N)]
indices = []

with open('file.txt', 'r') as file:
    for i in file:
        if -1 < int(i) < N:
            indices.append(int(i))

result = 1

# для проверки можно раскомментировать две строки ниже:
# print(lst)
# print(indices)

if indices:
    for i in indices:
        result *= lst[i]
    print(result)

else:
    print('Подходящих множителей нет')
