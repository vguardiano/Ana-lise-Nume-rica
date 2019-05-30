# def numberToBinary(number):
#     if number == 0:
#         return "0"
#     binary = ''
#     while number:
#         if number & 1 == 1:
#             binary = "1" + binary
#         else:
#             binary = "0" + binary
#         number //= 2
#     return binary
#
# print(numberToBinary(10))
#
# def binaryToDecimal(binary):
#     number = 0
#     for i, j in enumerate(binary):
#         number += int(j) * (2 ** (len(binary)-(i+1)))
#     return number
#
# print(binaryToDecimal("1100"))
#
# def d2b(decimal):
#     binary = ''
#     divisor = 1
#     while divisor:
#         divisor = decimal // 2
#         remainder = decimal - 2 * divisor
#         binary = str(remainder) + binary
#         decimal = divisor
#     return int(str(remainder) + binary)

import decimal
import math

decimal.getcontext().prec = 8
decimal.getcontext().rounding = decimal.ROUND_FLOOR

# # # # # #
#
# 2. Find the largest interval in which p∗ must lie to approximate p with relative
#   error at most 10^−4 for each value of p.
#
# # # # # #

def interval(p, n):
    return (float(decimal.Decimal(p)*decimal.Decimal(1-10**(-n))), float(decimal.Decimal(p)*decimal.Decimal(1+10**(-n))))
    # return (decimal.Decimal(p)/1*decimal.Decimal(1-10**(-n))/1, decimal.Decimal(p)/1*decimal.Decimal(1+10**(-n)))

print(interval(math.pi, 4))
print(interval(math.e, 4))
print(interval(2**(1/2), 4))
print(interval(7**(1/3), 4))

print("\n"*2)

# # # # # #
#
# 7. Use three-digit chopping arithmetic to perform the following calculations. Compute the absolute error
#   and relative error with the exact value determined to at least five digits.
#
# # # # # #

decimal.getcontext().prec = 3
decimal.getcontext().rounding = decimal.ROUND_FLOOR

def addition(x, y):
    return decimal.Decimal(decimal.Decimal(x)/1 + decimal.Decimal(y)/1)/1

def subtraction(x, y):
    return decimal.Decimal(decimal.Decimal(x) - decimal.Decimal(y))

def multiplication(x, y):
    return decimal.Decimal(decimal.Decimal(x) * decimal.Decimal(y))

def division(x, y):
    if decimal.Decimal(y) != 0:
        return decimal.Decimal(decimal.Decimal(x) / decimal.Decimal(y))

def absolute_error(p, float_p):
    return decimal.Decimal(abs(p - float(float_p)))/1

def relative_error(p, float_p):
    if p != 0:
        return decimal.Decimal(abs(p - float(float_p))/abs(p))/1

a = 133 + 0.921
float_a = addition(133, 0.921)
print("a)", float_a, absolute_error(a, float_a), relative_error(a, float_a))

b = 133 - 0.499
float_b = subtraction(133, 0.499)
print("b)", float_b, absolute_error(b, float_b), relative_error(b, float_b))

c = (121 - 0.327) - 119
float_c = subtraction(subtraction(121, 0.327), 119)
print("c)", float_c, absolute_error(c, float_c), relative_error(c, float_c))

d = (121 - 119) - 0.327
float_d = subtraction(subtraction(121, 119), 0.327)
print("d)", float_d, absolute_error(d, float_d), relative_error(d, float_d))

e = (13/14-6/7)/(2*math.e-5.4)
# float_e = division(subtraction(division(13, 14), division(6, 7)), subtraction(multiplication(2, math.e), 5.4))
float_e = division(subtraction(13/14, 6/7), subtraction(2*math.e, 5.4))
print("e)", float_e, absolute_error(e, float_e), relative_error(e, float_e))

f = -10*math.pi+6*math.e-3/62
float_f = subtraction(addition(multiplication(-10, math.pi), multiplication(6, math.e)), division(3, 62))
# float_f = subtraction(addition(-10*math.pi, 6*math.e), 3/62)
print("f)", float_f, absolute_error(f, float_f), relative_error(f, float_f))
