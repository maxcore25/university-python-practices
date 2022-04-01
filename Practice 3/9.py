import numpy as np
import matplotlib.pyplot as plt
import random


def distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def is_happy(data, human_x, human_y, xn, yn, t):
    neighbours = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = human_x + i
            y = human_y + j
            if x == xn:
                x = 0
            if y == yn:
                y = 0
            if data[human_x, human_y] == data[x, y]:
                neighbours[z] = 1
            z += 1
    my_favourite_neighbour = -1
    for i in range(8):
        if neighbours[i] == 1:
            my_favourite_neighbour += 1
    if float(my_favourite_neighbour / 8) >= t:
        return True
    else:
        return False


def main():
    population = 9000
    print('Размер популяции:', population)

    x = y = 100
    print('Размер сетки:', x, 'x', y)

    group1_percentage = 30
    print('Население 1 группы агентов (в процентах):', group1_percentage)

    group2_percentage = 70
    print('Население 2 группы агентов (в процентах):', group2_percentage)

    t = 0.5
    print('Пороговое значение толерантности:', t)

    n = 500000
    print('Количество шагов моделирования:', n)

    # генерация поля
    fig, ax = plt.subplots(ncols=2)
    data = np.random.randint(1, 2, (y, x))

    # генерация пустых клеток на поле
    empty = x * y - population
    i = 0
    happy = is_happy_list = []
    while i < empty:
        ex = int(random.uniform(0, x))
        ey = int(random.uniform(0, y))
        if data[ex, ey] == 1:
            data[ex, ey] = 0
        else:
            i -= 1
        i += 1

    # генерация клеток второй группы на поле
    another_population = int(group2_percentage / 100 * population)
    i = 0
    while i < another_population:
        ex = int(random.uniform(0, x))
        ey = int(random.uniform(0, y))
        if data[ex, ey] == 1:
            data[ex, ey] = 3
        else:
            i -= 1
        i += 1
    ax[0].imshow(data)

    i = 0
    while i < n:
        is_happy_amount = 0
        happy.append(float(is_happy_amount / population * 100))
        is_happy_list.append(i)
        empty = False
        ex = int(random.uniform(0, x))
        ey = int(random.uniform(0, y))

        new_x = new_y = 0
        if not is_happy(data, ex, ey, x, y, t):
            while not empty:
                new_x = int(random.uniform(0, x))
                new_y = int(random.uniform(0, y))
                if data[new_x, new_y] == 0:
                    empty = True
                    data[new_x, new_y] = data[ex, ey]
                    data[ex, ey] = 0
        i += 1

    ax[1].imshow(data)
    plt.show()
    plt.scatter(is_happy_list, happy)
    plt.show()


if __name__ == '__main__':
    main()
