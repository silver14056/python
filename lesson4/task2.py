"""
def calc1(a, b):
    return a + b
"""

calc1 = lambda a, b: a + b


def calc2(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))


math(calc1, 5, 45)
math(lambda a, b: a + b, 5, 45)

math(calc2, 5, 45)
