from sympy import *
import re


x = symbols('x')


pow_dict = {
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
    "⁷": "7",
    "⁸": "8",
    "⁹": "9",
    "⁰": "0"
}


def check_poly(check):
    try:
        eval(decode(check))
        return True
    except:
        return False


def decode(polyn):
    polyn = polyn.replace("X", "x").replace("Х", "x").replace("х", "x").replace(",", ".")
    polyn = polyn.split("=")[0].strip()
    for k, v in pow_dict.items():
        polyn = polyn.replace(k, v)
    polyn = re.sub(r"(x)(\d+)", r"\1**\2", polyn)
    polyn = re.sub(r"(\d+)(x)", r"\1*\2", polyn)
    polyn = re.sub(r"\^", "**", polyn)
    return polyn


def sum_poly(poly_one, poly_two):
    return str(eval(poly_one) + eval(poly_two))


def encode(polyn):
    polyn = re.sub(r"(\d+)\*(x)", r"\1\2", polyn)
    polyn = polyn.replace("**", "")
    powers = re.findall(r"x([^ ]+)", polyn)
    ind_pow_dict = {}
    for power in powers:
        power_copy = power
        for k, v in pow_dict.items():
            power_copy = power_copy.replace(v, k)
        ind_pow_dict[f'!{power}!'] = power_copy
    polyn = re.sub(r"x([^ ]+)", r"x!\1!", polyn)
    for k, v in ind_pow_dict.items():
        polyn = polyn.replace(k, v)
    polyn += ' = 0'
    return polyn
