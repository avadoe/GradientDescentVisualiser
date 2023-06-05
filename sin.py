import numpy as np
import random
import math
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

x = np.arange(-5, 5, 0.1)
y = f(x)

x_random = (random.random() - 0.5) * 20 * np.pi
y_random = f(x_random)

curr_point = (np.pi / 2, f(np.pi / 2))

learning_rate = 5e-3

for _ in range(1000):
    x_new, y_new = curr_point[0] - learning_rate * df(x=curr_point[0]), curr_point[1] - learning_rate * df(x=curr_point[1])
    curr_point = (x_new, y_new)
    
    plt.plot(x, y)
    plt.scatter(x_new, y_new, color='red')
    plt.pause(1e-3)
    plt.clf()