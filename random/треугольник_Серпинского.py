import random
import matplotlib.pyplot as plt



def plot(points):

    xs = [x for (x, y) in points]
    ys = [y for (x, y) in points]

    plt.plot(xs, ys, 'g.')
    plt.savefig('triangl.png')


def sierpinski(n):

    vertices = [(0.0, 0.0), (3.5, 2.0), (1.0, 3.5)]
    points = []

    # выбираем начальную вершину
    x, y = random.choice(vertices)

    for i in range(n):

        # выбираем новую точку
        new_x, new_y = random.choice(vertices)

        # получам середину
        x = (new_x + x) / 2.0
        y = (new_y + y) / 2.0

        points.append((x, y))


    plot(points)


# из скольки точек будет состоять треугольник
n = int(input())
sierpinski(n)