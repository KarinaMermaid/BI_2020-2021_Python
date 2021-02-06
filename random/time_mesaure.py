# Замерьте время вычисления чисел от 0 до 1 из равномерного распределения с помощью модуля random и модуля
# numpy, изобразите зависимость времени вычисления от количества вычисляемых чисел для них. Другими
# словами - по x идёт то, сколько чисел за прогон вы взяли от 0 до 1, а по y - время, которое это заняло.
# И сравните время выполнения в numpy и в random)

import numpy as np
import time as time_ns
import matplotlib.pyplot as plt
import random
x = int(input())
y = []

for i in range(x):
    start = time_ns.time()
    a = np.random.uniform(0, 1, x)
    end = time_ns.time()
    y.append(end - start)
print(y)

xs = range(x)
ys = y
plt.plot(xs, ys)
plt.savefig('plot.png')

z = []
for i in range(x):
    start = time_ns.time()
    b = random.uniform(0, 1)
    end = time_ns.time()
    z.append(end - start)
print(z)
xt = range(x)
yt = z
plt.plot(xt, yt)
plt.savefig('plot_2.png')