"""
# <center>**Beluga whale optimization code**</center>

## Introduction

Beluga whale optimization (BWO), a novel swarm-based metaheuristic algorithm inspired by beluga whale behaviors, we implemented the novel algorithm in this code to solve an optimization issue. BWO comprises three phases: exploration, exploitation, and whale fall, which correlate to the behaviors of pair swimming, preying, and whale falling.

## Goal
optimize the fitness function to get the optimal position of whale.

## Input

1. The random positions of the whales
2. upper bound of the search space
3. lower bound of the search space
4. dimensions of the search space
5. fitness function

## Output
1. best fitness value
2. best position of a whale

## Experimental protocol

1. Import required packages
2. Define different fitness functions to test the algorithm
3. Set the required parameters for the algorithm **(fitness function, max number of iterations ,dim ,ub, lb)**
4. Set random positions for the whales based on the search space
5. Loop over the max number of iterations.
6. Loop over the whales.
7. Define a list the holds The probabilities in exploration or exploitation and save it in the variable called **bf**.
8. If it's exploration **(bf > 0.5)**
    1. Generate pj (j = 1,2,…,d) randomly from dimension
    2. Choose a beluga whale Xr randomly
    3. Update new position of i-th beluga whale
9. If it's exploitation **(bf <= 0.5)**.
    1. Update the random jump strength **C1** and calculate the **Levy flight function**
    2. Update new position of **i-th** beluga whale
10. Check the boundaries of new positions and evaluate the fitness values
11. if **bf <= Wf** **(whale falls)**
    1. Update the step factor C2
    2. Calculate the step size Xstep
    3. Update new position of **i-th** beluga whale
    4. Check the boundaries of new position and calculate fitness value
12. Find the current best solution **P\***
13. Update the iteration by *1*


### Import required packages.
"""


import random
import math  # cos() for Rastrigin
import copy  # array-copying convenience
import sys  # max float
from fitness_functions import set_params
import numpy as np
import matplotlib.pyplot as plt

"""### Intialization of the whales position randomly."""

# whale class
# REF:- https://www.geeksforgeeks.org/implementation-of-whale-optimization-algorithm/?ref=rp
class whale:
    def __init__(self, fitness, dim, ub, lb, seed):
        """
        Initialize fitness values and random positions for whales.
        """
        self.rnd = random.Random(seed)
        self.position = [0.0 for i in range(dim)]
        for i in range(dim):
            #position
            self.position[i] = ((ub - lb) * self.rnd.random() + lb)
        self.fitness = fitness(self.position)  # curr fitness

"""### The BWO algorithm."""

def bwo(function_name, MAX_T, num_of_whales, *args):
    
    MAX_T = int(MAX_T)
    num_of_whales = int(num_of_whales)
    fitness, dim, lb, ub = set_params(function_name)
    
    whalePopulation = [whale(fitness, dim, ub, lb, i) for i in range(num_of_whales)]
    # compute the value of best_position and best_fitness in the whale Population
    best_fitness = sys.float_info.max #set Fbest to the maximum float value.
    
    for i in range(num_of_whales):  # check each whale
        #if fitness is of the less than Fbest
        if whalePopulation[i].fitness < best_fitness:
            #set whale fitness to Fbest
            best_fitness = whalePopulation[i].fitness
            #set the position of this whale to the best position.
            best_whale_position = copy.copy(whalePopulation[i].position) 
    
    #to hold the best fitness values
    fitness_list = []
    #to hold the best whales position
    whales_positions = []
    
    t = 0 #iteration
    iterations = []
    best_whale_position = np.array(best_whale_position, dtype=np.float32)
    
    decay_value = 0
    while t < MAX_T:
        bf = []
        for i in range(num_of_whales):
            b0 = random.random() - decay_value
            bf.append(b0*(1-((t)/(2*MAX_T)))) # The probabilities in exploration or exploitation
        decay_value += 0.005
        
        for i in range(num_of_whales):  # check each whale
            whalePopulation[i].position = np.array(whalePopulation[i].position, dtype=np.float32)
            random_whale = np.array(random.choice(whalePopulation).position, dtype=np.float32)
            
            if bf[i] > 0.5:
                # In the exploration phase
                r1 = random.random()
                r2 = random.random()
                pj = np.arange(0,dim)
                j = np.random.choice(pj, 1)[0] 
                #if the random dimension was even
                if j % 2 == 0:
                    # update the position of the whale.
                    whalePopulation[i].position[j] = whalePopulation[i].position[j] + (random_whale[0] - whalePopulation[i].position[j])*(1 -r1)*math.sin(360*r2)
                 #if the random dimension was even
                elif j % 2 != 0:
                    # update the position of the whale.
                    whalePopulation[i].position[j] = whalePopulation[i].position[j] + (random_whale[0] - whalePopulation[i].position[j])*(1 -r1)*math.cos(360*r2)
                    
            elif bf[i] <= 0.5:
                # In the exploitation phase
                r3 = random.random()
                r4 = random.random()
                beta=3/2
                numerator = math.gamma( 1 + beta ) * math.sin(math.pi * beta / 2)
                denominator = math.gamma((1 + beta) / 2) * beta * math.pow(2, (beta -1) /2)  
                sigma = (numerator / denominator) ** (1 / beta)
                u = np.random.normal(0, 0.1, 1)[0]
                v = np.random.normal(0, 0.1, 1)[0]
                s = (u * sigma) / (abs(v) ** (1 / beta))
                #  Levy flight function
                Lf = 0.05 * s
                #random jump strength that measuring the intensity of Levy flight.
                C1 = 2 * r4 * ( 1 - t - MAX_T)
                
                # update the position of the whale.
                array_diff = random_whale - whalePopulation[i].position
                whalePopulation[i].position = (r3 * best_whale_position) - (r4 * whalePopulation[i].position) + C1 * Lf * array_diff
                
            #Check and clib the boundaries of new positions
            whalePopulation[i].position = np.where(whalePopulation[i].position> ub, ub, whalePopulation[i].position)
            whalePopulation[i].position = np.where(whalePopulation[i].position< lb, lb, whalePopulation[i].position)

            #return the fitness value if it's less than the previous one, and the best position of the whale.
            new_fitness = fitness(whalePopulation[i].position)
            if new_fitness == 0.0:
                print(f"Iter = {t}:- fitness optimized from {round(best_fitness,4)} to {round(new_fitness,4)} (Global optimum)")
                best_fitness = new_fitness
                best_whale_position = copy.copy(whalePopulation[i].position)
                fitness_list.append(best_fitness)
                whales_positions.append(best_whale_position)
                iterations.append(t)
                return best_fitness, best_whale_position, fitness_list, whales_positions, iterations
            
            #return the fitness value if it's less than the previous one, and the best position of the whale.
            if new_fitness < best_fitness and new_fitness > -1:
                print(f"Iter = {t}:- fitness optimized from {round(best_fitness,4)} to {round(new_fitness,4)}")
                best_fitness = new_fitness
                best_whale_position = copy.copy(whalePopulation[i].position)
                fitness_list.append(best_fitness)
                whales_positions.append(copy.copy(whalePopulation[i].position))
                iterations.append(t)
                
        #the probability of whale fall
        WF = 0.1-0.05*(t/MAX_T);  # The probability of whale fall
        #step factor which is related to the probability of whale fall and population size
        C2 = 2 * WF * num_of_whales
        for i in range(num_of_whales): #check each whale
            if bf[i] <= WF:
                random_whale = np.array(random.choice(whalePopulation).position, dtype=np.float32)
                r5 = random.random()
                r6 = random.random()
                r7 = random.random()
                #step size of whale fall
                xstep = (ub - lb)*math.exp(-C2*t*MAX_T)
                whalePopulation[i].position = (r5 * whalePopulation[i].position) - (r6 * random_whale) + (r7 * xstep)
            
            #Check and clib the boundaries of new positions
            whalePopulation[i].position = np.where(whalePopulation[i].position> ub, ub, whalePopulation[i].position)
            whalePopulation[i].position = np.where(whalePopulation[i].position< lb, lb, whalePopulation[i].position)
            
            #return the fitness value if it's zero (global optimal) and break the loop, and the best position of the whale.
            new_fitness = fitness(whalePopulation[i].position)
            if new_fitness == 0.0:
                print(f"Iter = {t}:- fitness optimized from {round(best_fitness,4)} to {round(new_fitness,4)} (Global optimum)")
                best_fitness = new_fitness
                best_whale_position = copy.copy(whalePopulation[i].position)
                fitness_list.append(best_fitness)
                whales_positions.append(best_whale_position)
                iterations.append(t)
                return best_fitness, best_whale_position, fitness_list, whales_positions, iterations
            
            #return the fitness value if it's less than the previous one, and the best position of the whale.
            if new_fitness < best_fitness and new_fitness > -1:
                print(f"Iter = {t}:- fitness optimized from {round(best_fitness,4)} to {round(new_fitness,4)}")
                best_fitness = new_fitness
                best_whale_position = copy.copy(whalePopulation[i].position)
                fitness_list.append(fitness(whalePopulation[i].position))
                whales_positions.append(copy.copy(whalePopulation[i].position))
                iterations.append(t)
        t += 1
    
    return best_fitness, best_whale_position, np.array(fitness_list), np.array(whales_positions), iterations

def plot(iterations, fitness_list):
    if iterations != []:
        plt.figure(figsize=(10,8))
        plt.xlabel("iteration number")
        plt.ylabel("fitness value")
        plt.plot(iterations , fitness_list)
        plt.title("Fitness value over number of iterations")
    else:
        print("I couldn't optimize using this function.")
if __name__ == "__main__":
    
    best_fitness, best_position, fitness_list, positions_list, iterations = bwo(*sys.argv[1:])
    print(f"best fitness value {best_fitness}")
    print(f"best whale position {best_position}")
    plot(iterations, fitness_list)

