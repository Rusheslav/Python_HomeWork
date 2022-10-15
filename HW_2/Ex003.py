N = '0'
while not (N.isdigit() and int(N) > 0):
    N = input('Введите натуральное число: ')

print(sum([(1 + 1/n) ** n for n in range(1, int(N) + 1)]))
