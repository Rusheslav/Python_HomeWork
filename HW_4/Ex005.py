# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_lst(file: str) -> list:
    with open(file, 'r') as f:
        s = f.readline()[:-4]
        print(s)                                    # Оставляю для удобства проверки в консоли
    s = s.replace('+ ', '+').replace('- ', '-')
    if s[0] != '-':
        s = '+' + s
    return s.split()


def get_dict(lst: list) -> dict:
    dct = {}
    for i in lst:
        sign = i[0]
        i = i[1:]
        coef = i
        power = 0
        if 'x' in i:
            coef = i.split('x')[0] if i.split('x')[0] else '1'
            if '^' in i:
                power = int(i.split('^')[1])
            else:
                power = 1
        dct[power] = [sign, coef]
    return dct


def sum_els(lst_a: list, lst_b: list) -> list or None:
    sign_a, sign_b = lst_a[0], lst_b[0]
    coef_a, coef_b = int(lst_a[1]), int(lst_b[1])
    if sign_a == '+' and sign_b == '+':
        coef = coef_a + coef_b
    elif sign_a == '+' and sign_b == '-':
        coef = coef_a - coef_b
    elif sign_a == '-' and sign_b == '+':
        coef = - coef_a + coef_b
    else:
        coef = - coef_a - coef_b

    if coef > 0:
        return ['+', str(coef)]
    elif coef < 0:
        return ['-', str(coef)[1:]]
    else:
        return None


a, b = map(get_lst, ['file1.txt', 'file2.txt'])
print(a, b, sep='\n')                               # Оставляю для удобства проверки в консоли
a, b = map(get_dict, [a, b])
print(a, b, sep='\n')                               # Оставляю для удобства проверки в консоли

for k, v in b.items():
    if k not in a:
        a[k] = v
    elif sum_els(a[k], v):
        upd_elt = sum_els(a[k], v)
        a[k] = upd_elt
    else:
        del a[k]

res = ''
for k, v in sorted(a.items(), reverse=True):
    if k > 1 and v[1] != '1':
        res += f' {v[0]} {v[1]}x^{k}'
    elif k > 1:
        res += f' {v[0]} x^{k}'
    elif k == 0:
        res += f' {v[0]} {v[1]}'
    elif k == 1 and v[1] != '1':
        res += f' {v[0]} {v[1]}x'
    elif k == 1:
        res += f' {v[0]} x'

if not res:
    res = '0 = 0'
elif res[0:2] == ' +':
    res = res[3:] + ' = 0'
else:
    res = '- ' + res[3:] + ' = 0'

print(res)                                          # Оставляю для удобства проверки в консоли

with open('file3.txt', 'w') as f:
    f.write(res)
