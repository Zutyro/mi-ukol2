from multiprocessing.managers import convert_to_error

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
    best_result = 0
    best_point = 0
    convergence_points = []
    convergence_results = []
    climb_results = []
    climb_points = []
    for i in range(max_iterations):
        for x in range(population):
            coords = [random.gauss(center_point[j],standard_deviation) for j in range(dimensions)]
            # outofdomain = False
            # for coord in coords:
            #     if coord not in domain:
            #         outofdomain = True
            # if outofdomain:
            #     continue
            if best_result == 0:
                best_result = test_function(coords)
                best_point = coords
            if test_function(coords) < best_result:
                best_result = test_function(coords)
                best_point = coords
        center_point = best_point
        climb_points.append(best_point)
        climb_results.append(best_result)
        if len(convergence_points) == 0:
            convergence_points.append(best_point)
            convergence_results.append(best_result)
        if convergence_results[len(convergence_points)-1] > best_result:
            convergence_points.append(best_point)
            convergence_results.append(best_result)
    if dimensions == 2:
        climb_points = np.array(climb_points).T
        xx,yy = np.meshgrid(np.linspace(domain[0],domain[1],500), np.linspace(domain[0],domain[1],500))
        zz = test_function((xx,yy))
        fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # ax.plot_surface(xx, yy, zz)
        plt.pcolor(xx, yy, zz)
        plt.scatter(climb_points[0],climb_points[1],color='Red')
        # ax.view_init(azim=0, elev=90)
        plt.show()
    plt.step(convergence_results,range(len(convergence_results)))
    plt.show()
    print(f'Best result:{convergence_results[len(convergence_results)-1]} in {convergence_points[len(convergence_points)-1]}')






if __name__=='__main__':
    hill_climber(200,2,5,20,2)
