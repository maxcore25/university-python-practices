import math


# 1) whitespace before '('
def ex1_1(y):
    return math.sqrt (25)  # Перед (25 пробел

ex1_1(1)

# 2) missing whitespace around operator
def ex1_2(y):
    return 57* 2  # После 57 сразу *

ex1_2(4)

# 3) missing whitespace after ','
def ex1_3(x, y):
    return x + y

ex1_3(6,8) # 6,8

# 4) unexpected spaces around keyword / parameter equals
def ex1_4(x= '1', y='2'):  # Перед '1' лишний пробел
    return x

ex1_4('a', 'b')

# 5) expected 2 blank lines, found 1
import sys  # После import должны быть 2 пустые строки

def ex1_5(x='1', y='2'):  # Перед '1' лишний пробел
    return x

ex1_5('a', 'b')
x = 0

# 6) multiple statements on one line (colon)
if x > 5: y = 10  # y = 10 должно быть написано на новой строке

# 7) multiple statements on one line (semicolon)
x = 5; y = 10  # y = 10 должно быть написано с новой строки. после x = 5 не должно быть ';'

# 8) comparison to None should be 'if cond is None:'
if x == None:  # Сравнение с None лучше выполнять с помощью is / is not None
    print("Do something")

# 9) comparison to True should be 'if cond is True:' or 'if cond:'
if y == True:  # Необходимо написать if y is True: или просто if y:
    print('a')