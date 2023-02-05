import numpy as np
import random
import math


# sphere fitness function
def fitness_sphere(position):
    position = np.array(position) 
    return np.sum(position * position)

# powell sum fitness function
def fitness_powell_sum(position):
    fitness_value = 0.0
    for i in range(len(position)):
        fitness_value += (abs(position[i]) ** (i+1))
    return fitness_value

# Schwefel’s 1.2 fitness function
def fitness_Schwefels(position):
    fitness_value = 0.0
    for i in range(len(position)):
        fitness_value += (sum(position) ** 2)
    return fitness_value

#Rosenbrock fitness function
def fitness_rosenbrock(position):
    fitness_value = 0.0
    for i in range(len(position) -1):
        fitness_value += ((100*(position[i+1] - position[i] ** 2) ** 2) + (position[i] - 1) ** 2)
    return fitness_value

#step function
def fitness_step(position):
    fitness_value = 0.0
    for i in range(len(position)):
        fitness_value += (position[i] + 0.5) ** (2)
    return fitness_value

#Quartic funtion
def fitness_quartic(position):
    fitness_value = 0.0
    for i in range(len(position)):
        fitness_value += ((i+1) * (position[i] ** 4) + random.random())
    return fitness_value

#Zakharov function
def fitness_zakharov(position):
    fitness_value = None
    first = 0.0
    second = 0.0
    
    for i in range(len(position)):
        first += position[i] ** 2
        second += (0.5 * i * position[i])
    fitness_value = first + second ** 2 + second ** 4
    return fitness_value
#rastrigin function
def fitness_rastrigin(position):
    fitness_value = 0.0
    for i in range(len(position)):
        xi = position[i]
        fitness_value += (xi ** 2) - (10 * math.cos(2 * math.pi * xi)) + 10
    return fitness_value

def set_params(function_name):
    if function_name == "F1":
        return fitness_sphere, 30, -100, 100
    if function_name == "F3":
        return fitness_powell_sum, 30, -1, 1
    if function_name == "F4":
        return fitness_Schwefels, 30, -100, 100
    if function_name == "F6":
        return fitness_rosenbrock, 30, -30, 30
    elif function_name == 'F7':
        return fitness_step, 30 , -100, 100
    elif function_name == 'F8':
        return fitness_quartic, 30 , -1.28, 1.28
    elif function_name == 'F9':
        return fitness_zakharov, 30 , -5, 10
    elif function_name == 'F13':
        return fitness_rastrigin, 30, -5.12, 5.12