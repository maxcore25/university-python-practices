import random


def ex4_1(x):
    # Задание 1
    x = x + x  # 2
    x = x + x  # 4
    x = x + x + x  # 12
    return x


def ex4_2(x):
    # Задание 2
    x = x + x  # 2
    x = x + x  # 4
    x = x + x  # 8
    x = x + x  # 16
    return x


def ex4_3(x):
    # Задание 3
    x = a  # 1
    z = a  # 1
    x = x + x  # 2
    x = x + x  # 4
    y = x + x  # 8
    x = z - y  # -7
    x = y - x  # 15
    return x


def ex4_4(x):
    # Задание 4
    x = a  # 1
    x = x + x  # 2
    x = x + x  # 4
    x = x + x  # 8
    x = x - a  # 7
    x = x + x  # 14
    x = x + x  # 28
    x = x + a  # 29
    return x


# Задача 10
def fast_mul(x, y):
    xy_sum = 0
    while x:
        if x % 2 != 0:
            xy_sum = y + xy_sum
        x = x // 2
        y = y * 2
    return xy_sum


def fast_pow(x, y):
    if not y:
        return 1
    if y == 1:
        return x
    result = 0
    y -= 1
    z = x
    x1 = x
    while y:
        result = 0
        while x:
            if x % 2 != 0:
                result = x1 + result
            x //= 2
            x1 *= 2
        x = result
        x1 = z
        y -= 1
    return result


def fast_mul_gen(x, y):
    result = 0
    print('Result =', result)
    while x:
        if x % 2 != 0:
            print('Result =', result, '+', y)
            result = y + result
        print('y = y +', y)
        x //= 2
        y *= 2
    print('Result =', result)


if __name__ == '__main__':
    # Задача 4
    a = int(input('Введите число: '))
    print(a, '* 12 =', ex4_1(a))
    print(a, '* 16 =', ex4_2(a))
    print(a, '* 15 =', ex4_3(a))
    print(a, '* 29 =', ex4_4(a))

    print('-----Автоматическое тестирование-----')

    for i in range(5):
        print('---------- Тест №', i, '----------')
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        print('x =', m)
        print('y =', n)
        print('Результат перемножения:', fast_mul(m, n))
        print('Результат возведения в', n, 'степень числа', m, ':', fast_pow(m, n))
        print('Проверка функции fast_mul_gen()')
        fast_mul_gen(m, n)
