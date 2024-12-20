# -*- coding: utf-8 -*-
"""grad_desc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V1Kp1QpHEEOanE06rZ7gLsKAk3E-FLp3
"""

import numpy as np

def loss_func(x):
    return x**2

def gradient_func(x):
    return 2 * x

x_1 = 12
step = 0.1
iterations = 12

def gradient_descent(x, step, iterations):
    for i in range(iterations):
        grad = gradient_func(x)
        x = x - step * grad
        print( f"{i+1}: x = {x:.3f}, Loss = {loss_func(x):.3f}" )
    return x

min_x = gradient_descent(x_1, step , iterations)
print( f"Минимум x: {min_x:.3f}" )