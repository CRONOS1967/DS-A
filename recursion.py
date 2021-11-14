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
    assert num >=0 and int(num) == num,'Please the number should be an +VE Integer'
    if num in {0,1}:
        return 1
    else:
        return num* factorials(num-1)
        
# Fabonacci numbers in recursion
# 'num' represents the element in faboncci series

def fabonacci(num):
    assert num >=0 and int(num) == num,'Please the number should be an +VE Integer'
    if num in[0,1]:
        return num
    else:
        return fabonacci(num-1) + fabonacci(num-2)