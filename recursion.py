# just call the function to see their action
# basic Rucrrsion function
# ----------------------------------------
# def recursivefun(parameters):
#     if exit from condition satisfied:
#         return some Value
#     else:
#         recursivefun(modifed parameter)
# -----------------------------------------

def count(doll):
    if doll == 1:
        print('last doll')
    else:
        print(doll)
        count(doll-1)
# Factorials using recursion


def factorials(num):
    assert num >= 0 and int(
        num) == num, 'Please the number should be an +VE Integer'
    if num in {0, 1}:
        return 1
    else:
        return num * factorials(num-1)

# Fabonacci numbers in recursion
# 'num' represents the element in faboncci series


def fabonacci(num):
    assert num >= 0 and int(
        num) == num, 'Please the number should be an +VE Integer'
    if num in [0, 1]:
        return num
    else:
        return fabonacci(num-1) + fabonacci(num-2)

# sum of digits of a postive integer using recursion

def sum(num):
    assert num >= 0 and int(
        num) == num, 'Please the number should be an +VE Integer'
    if num == 0:
        return 0
    else:
        return int(num % 10) + sum(int(num/10))

# Power of number using recursion

def poweOf(base,exp):
    assert exp >= 0 and int(
        exp) == exp, 'Please the exponet number should be an +VE Integer'
    if exp == 0:
        return 1
    if exp ==1:
        return base
    return base * poweOf(base,exp-1)

# finding GCD(Greatest common Divisor) of two numbers using recursion
#  using Euclidean algorithm

def gcd(num, num2):
    assert int(num) ==num and int(num2) == num2, 'The numbers must be integer only'
    if num<0:
        num= -1*num
    if num2 < 0:
        num2=-1*num2
    if num2==0:
        return num
    else:
        return gcd(num2, num % num2)
        
# convert a number from Decimal to Binary using recursion

def binary(num):
    assert int(num) ==num, 'The numbers must be integer only'
    if num == 0:
        return 0
    else:
        return (num % 2) + 10 * binary(int(num/2))