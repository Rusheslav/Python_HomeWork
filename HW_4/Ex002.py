# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def is_simple(num: int) -> bool:
    if num in [2, 3, 5]:
        return True
    if not num % 2 or not num % 3 or not num % 5 or num == 1:
        return False
    for i in range(7, num//7, 2):
        if not num % i:
            return False
    return True


N = input('Введите натуральное число N: ')
while not (N.isdigit() and N != '0'):
    N = input("Неверный ввод. Введите натуральное число: ")

N = int(N)
factors = set()
fac = 2
while not is_simple(N):
    while not N % fac:
        factors.add(fac)
        N //= fac
    fac += 1

factors.add(N)

print(sorted(list(factors)))
