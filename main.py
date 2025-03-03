import numpy as np
import matplotlib.pyplot as plt
import random

def test_domain(point_values, domain):
    for x in point_values:
        if x < domain[0] or x > domain[1]:
            return False
    return True

def sphere(point_values):
    sum1 = 0
    for x in point_values:
        sum1 = sum1 + (x ** 2)
    y = sum1
    return y

def trid(point_values):
    sum1, sum2 = 0, 0
    for j, x in enumerate(point_values):
        sum1 = sum1 + (x - 1) ** 2
        if j > 0:
            sum2 = sum2 + x * point_values[j - 1]
    y = sum1 - sum2
    return y

def schwefel(point_values):
    sum1 = 0
    for x in point_values:
        sum1 = sum1 + x * np.sin(np.sqrt(np.abs(x)))
    y = 418.9829 * len(point_values) - sum1
    return y

def dixonprice(point_values):
    sum1 = 0
    for j, x in enumerate(point_values):
        if j == 0:
            continue
        sum1 = sum1 + (j + 1) * (2 * (x ** 2) - point_values[j - 1]) ** 2
    y = (point_values[0] - 1) ** 2 + sum1
    return y

def rosenbrock(point_values):
    sum1 = 0
    for j, x in enumerate(point_values):
        if j == len(point_values) - 1:
            continue
        sum1 = sum1 + (100 * (point_values[j + 1] - x ** 2) ** 2 + (x - 1) ** 2)
    y = sum1
    return y


def hill_climber(max_iterations, dimensions: int, population, standard_deviation, function_type):
    domain = []
    match function_type:
        case 0:
            print('sphere')
            test_function = sphere
            domain = [-5.12,5.12]
        case 1:
            print('trid')
            test_function = trid
            domain = [-dimensions**2,dimensions**2]
        case 2:
            print('schwefel')
            test_function = schwefel
            domain = [-500,500]
        case 3:
            print('dixonprice')
            test_function = dixonprice
            domain = [-10,10]
        case 4:
            print('rosenbrock')
            test_function = rosenbrock
            domain = [-2.048,2.048]
        case _:
            raise ValueError('Function_type outside of range. Accepts values between 0 and 4')
    center_point = [random.uniform(domain[0], domain[1]) for i in range(dimensions)]
    print(center_point)
    print(test_function(center_point))




if __name__=='__main__':
    hill_climber(20,2,3,3,0)
    print(sphere([10,10]))