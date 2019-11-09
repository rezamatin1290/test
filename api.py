from os import sys

def is_infix(a):
    operator = ["*", "/", "-", "+", "^"]

    if a[0] in operator or a[-1] in operator:return False

    flag = 0
    for x in range(len(a)-1):
        if flag == 0:
            if not a[x+1] in operator:return False
            else: flag = 1
        elif flag  == 1:
            if  a[x+1] in operator:return False
            else: flag = 0

    return True



def is_prefix(a):
    if  is_infix(a):return False

    operators = {"^":1, "*" : 2, "/":2, "+":3, "-":3}

    if a[0] in operators:return True
    else: return False


def is_postfix(a):
    if is_infix(a): return False
    operators = {"^":1, "*" : 2, "/":2, "+":3, "-":3}

    if a[-1] in operators:return True
    else: return False


print("prefix : ", is_prefix(sys.argv[1]))
print("infix : ", is_infix(sys.argv[1]))
print("Postfix : ", is_postfix(sys.argv[1]))
