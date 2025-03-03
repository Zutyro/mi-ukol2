import numpy as np
import matplotlib.pyplot as plt
import random

def test_domain(point_values, domain):
    for x in point_values:
        if x < domain[0] or x > domain[1]:
            return False
    return True

def sphere(point_values):
    domain = [-5.12,5.12]
    if not test_domain(point_values, domain):
        return -99999
    sum1 = 0
    for x in point_values:
        sum1 = sum1 + (x ** 2)
    y = sum1
    return y

def trid(point_values):
    dimensions = len(point_values)
    domain = [-dimensions**2,dimensions**2]
    if not test_domain(point_values, domain):
        return -99999
    sum1, sum2 = 0, 0
    for j, x in enumerate(point_values):
        sum1 = sum1 + (x - 1) ** 2
        if j > 0:
            sum2 = sum2 + x * point_values[j - 1]
    y = sum1 - sum2
    return y

def schwefel(point_values):
    domain = [-500,500]
    if not test_domain(point_values, domain):
        return -99999
    sum1 = 0
    for x in point_values:
        sum1 = sum1 + x * np.sin(np.sqrt(np.abs(x)))
    y = 418.9829 * len(point_values) - sum1
    return y

def dixon(point_values):
    domain = [-10,10]
    if not test_domain(point_values, domain):
        return -99999
    sum1 = 0
    for j, x in enumerate(point_values):
        if j == 0:
            continue
        sum1 = sum1 + (j + 1) * (2 * (x ** 2) - point_values[j - 1]) ** 2
    y = (point_values[0] - 1) ** 2 + sum1
    return y

def rosenbrock(point_values):
    domain = [-2.048,2.048]
    if not test_domain(point_values, domain):
        return -99999
    sum1 = 0
    for j, x in enumerate(point_values):
        if j == len(point_values) - 1:
            continue
        sum1 = sum1 + (100 * (point_values[j + 1] - x ** 2) ** 2 + (x - 1) ** 2)
    y = sum1
    return y


def hill_climber(max_iterations, dimensions, population, standard_deviation):
    print('hello')


hill_climber(20,2,3,3)
