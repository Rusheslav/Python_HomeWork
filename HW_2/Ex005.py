from random import randint

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = len(lst) - 1

for i in range(l):
    j = randint(i + 1, l)
    lst[i], lst[j] = lst[j], lst[i]

print(lst)