from decimal import Decimal


def calculate(expr: str) -> tuple:
    expr = expr.replace(' ', '').replace('x', '*').replace('X', '*').replace('х', '*').replace('Х', '*').replace(',', '.')
    fin_expr = expr
    while '(' in expr:
        closing_index = expr.index(')')
        open_index = expr[:closing_index].rfind('(')
        inner_expr = expr[open_index + 1:closing_index]
        expr = expr[:open_index] + calculate(inner_expr)[0] + expr[closing_index + 1:]
        expr = expr.replace('+-', '-').replace('--', '+').replace('*-', 'm').replace('/-', 'd')

    signs = [expr[i] for i in range(len(expr)) if expr[i] in '/*+-md' and not (i == 0 and expr[i] == '-')]
    numbers = expr.replace('/', '*').replace('+', '*').replace('-', '*-').replace('m', '*').replace('d', '*').split('*')
    numbers = [Decimal(n) for n in numbers if n]

    def make_operation(sign: str) -> None:
        while sign in signs:
            sign_index = signs.index(sign)
            first_num = numbers[sign_index]
            second_num = numbers[sign_index + 1]
            if sign == '/':
                numbers[sign_index] = first_num / second_num
            elif sign == 'd':
                numbers[sign_index] = -first_num / second_num
            elif sign == '*':
                numbers[sign_index] = first_num * second_num
            elif sign == 'm':
                numbers[sign_index] = -first_num * second_num
            elif sign == '+' or '-':
                numbers[sign_index] = first_num + second_num
            del numbers[sign_index + 1]
            del signs[sign_index]

    for i in '/d*m+-':
        make_operation(i)

    return str(Decimal.normalize(numbers[0])) if '.' in str(numbers[0]) else str(numbers[0]), fin_expr
