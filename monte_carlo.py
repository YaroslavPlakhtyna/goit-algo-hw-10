import random

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return np.log(x)

# Визначення методу Монте-Карло для обчислення інтегралу функції
def monte_carlo_simulation(a, b, num_experiments=100):
    average_area = 0

    # Визначення верхньої межі прямокутника
    Y = max(f(a), f(b))
    for _ in range(num_experiments):
        # Генерація випадкових точок, що належать прямокутнику
        points = [(random.uniform(a, b), random.uniform(0, Y)) for _ in range(15000)]
        # Вибірка точок, що належать простору під даною функцією
        inside_points = [point for point in points if point[1] <= f(point[0])]

        M = len(inside_points)
        N = len(points)
        # Обчислення площі за допомогою метода Монте-Карло
        area = (M / N) * (abs(b - a) * Y)

        # Додавання до сумарної площі усіх експериментів
        average_area += area

    # Визначення середньої площі серед усіх значень експериментів
    average_area /= num_experiments
    return average_area


if __name__ == "__main__":
    a = 20  # Нижня межа
    b = 80  # Верхня межа

    # Обчислення інтеграла за допомогою метода Монте-Карло
    mc_res = monte_carlo_simulation(a, b)
    print("Інтеграл (Monte-Carlo): ", mc_res)

    # Обчислення інтеграла за допомогою quad
    quad_res, error = spi.quad(f, a, b)
    print("Інтеграл (quad): ", quad_res)

    # Створення діапазону значень для x
    x = np.linspace(1, 100, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.text(0.5 * (a + b), 0.5, "Monte-Carlo: {:.4f}\nscipy.integrate.quad: {:.4f}".format(mc_res, quad_res),
    horizontalalignment='center', fontsize=10)

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = log(x) від ' + str(a) + ' до ' + str(b))

    plt.grid()
    plt.show()