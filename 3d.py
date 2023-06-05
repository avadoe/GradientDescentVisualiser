import numpy as np
import random
import matplotlib.pyplot as plt

def z(x, y):
    return np.sqrt(1 - (x ** 2) - (y ** 2))

def df(x, y):
    df_x = (1 / (2 * np.sqrt(1 - x ** 2 - y ** 2))) * (- 2 * x)
    df_y = (1 / (2 * np.sqrt(1 - x ** 2 - y ** 2))) * (- 2 * y)
    return df_x, df_y


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = z(X, Y)

random_x = random.random() / 2
random_y = random.random() / 2
random_z = z(random_x, random_y)

curr_point = (random_x, random_y, random_z)

learning_rate = 5e-3

ax = plt.subplot(projection='3d', computed_zorder=False)

for _ in range(1000):
    dX, dY = df(curr_point[0], curr_point[1])
    X_new, Y_new = curr_point[0] - learning_rate * dX, curr_point[1] - learning_rate * dY
    curr_point = (X_new, Y_new, z(X_new, Y_new))
    ax.plot_surface(X, Y, Z, cmap='YlGnBu')
    ax.scatter(curr_point[0], curr_point[1], curr_point[2], color='black', zorder=1)
    plt.pause(0.001)
    ax.clear()
