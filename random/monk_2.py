# Сделайте функцию для проверки является ли список отсортированным (без использования sorted или sort).
# Затем реализуйте monkey sort , а потом визуализируйте следующее: распределение времени работы алгоритма
# от размера сортируемого списка. То есть по x идёт размер массива, а по y - среднее время нескольких прогонов
# и их отклонение (или дисперсия)
from random import shuffle, random
import timeit
import statistics
import matplotlib.pyplot as plt
setup = '''
from random import shuffle, random
import time as time_ns




def is_sorted(data) -> bool:
    # определяет отсортированны ли данные
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

def bogosort(data: list) -> list:
    # перемешивает данные, пока не отсортируются
    # работаем с копией данных, чтобы исходные оставались без изменений
    copi = data.copy()
    while not is_sorted(copi):
        shuffle(copi)
    return copi
'''
lenght_int = int(input()) #длина списка

def mass_generation (lenght):
    # генерирует список случайных чисел  длиной lenght_int
    return [random() for x in range(lenght)]


# генерирует lenght_int списков из случайных чисел длиной от 0 до lenght_int
sp = [mass_generation(x+1) for x in range(lenght_int)]
mas = []
for i in sp:
    a = f'bogosort({i})'
    ans = timeit.repeat(stmt = a, repeat=5, number=1000, setup=setup)
    mas.append(ans)


plt.boxplot(mas)
plt.savefig('plot_mnk.png')

