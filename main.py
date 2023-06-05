import numpy as np
import random
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

def df(x):
    return 2 * x

x = np.arange(-100, 100, 0.05)
y = f(x)

x_random = (random.random() - 0.5) * 200
y_random = f(x_random)

curr_point = (x_random, y_random)
learning_rate = 5e-3

for _ in range(1000):
    x_new, y_new = curr_point[0] - learning_rate * df(x=curr_point[0]), curr_point[1] - learning_rate * df(x=curr_point[1])
    curr_point = (x_new, y_new)
    
    plt.plot(x, y)
    plt.scatter(x_new, y_new, color='red')
    plt.pause(1e-3)
    plt.clf()