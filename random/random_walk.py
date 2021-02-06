#Визуализируйте random walk в 2-мерном пространстве, где вы начинаете в (0, 0)
# и можете перемещаться вверх, вниз, вправо и влево. Как визуализировать - скаттерплот, где по x - x, а по y - y

import numpy as np
import matplotlib.pyplot as plt
import random


n = int(input()) # вводим число шагов
step_set = ['Up', 'Down', 'Left', 'Right'] # какие шаги мы можем совершать

# задаем оси
x = np.zeros(n)
y = np.zeros(n)

# сами шаги. Увы, довольно  топорно...
for i in range(1, n):
    step = random.choice(step_set)
    if step == 'Right':
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif step == 'Left':
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif step == 'Up':
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    elif step == 'Down':
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

plt.plot(x, y)
plt.savefig('plot_random_walk.png')