N = '0'
while not (N.isdigit() and int(N) > 0):
    N = input('Введите натуральное число: ')

res = []
for i in range(1, int(N) + 1):
    for j in range(1, i):
        i *= j
    res.append(i)

print(res)
