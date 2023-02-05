<h1 align='center'>Beluga whale optimization code</h1>

## Introduction 
Beluga whale optimization (BWO), a novel swarm-based metaheuristic algorithm inspired by beluga whale behaviors, we implemented the novel algorithm in this code to solve an optimization issue. BWO comprises three phases: exploration, exploitation, and whale fall, which correlate to the behaviors of pair swimming, preying, and whale falling.

## Goal
optimize the fitness function to get the optimal position of whale.

## Input

1. fitness function.
2. number of max iterations.
3. number of whales.

## Output
1. best fitness value
2. best position of a whale

## Experimental protocol

1. Import required packages
2. Define different fitness functions to test the algorithm
3. Set the required parameters for the algorithm **(fitness function, max number of iterations, number of whales)**
4. Set random positions for the whales based on the search space
5. Loop over the max number of iterations.
6. Loop over the whales.
7. Define a list the holds The probabilities in **exploration** or **exploitation** and save it in the variable called **bf**.
8. If it's exploration **(bf > 0.5)**
    1. Generate **pj (j = 1,2,…,d)** randomly from dimension
    2. Choose a *beluga whale* **Xr** randomly
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

<p align="center">
  <img src="https://github.com/Eng-ZeyadTarek/Nature-Inspired-Optimization-Algorithms/blob/main/Beluga%20Whales%20Optimization%20Code/Beluga%201.JPG" alt='Behaviors of beluga whales'>
</p>

<p align="center">
    <strong> Fig. 1 </strong> Behaviors of beluga whales, (a) swim, corresponding to exploration phase; (b) foraging, corresponding to exploitation phase, (c) whale fall, for whale fall phase. Source: https://constative.com/animals/whale-watching, https://www.sealuxe.ca/blog/narwhal
</p>

<p align="center">
  <img src="https://github.com/Eng-ZeyadTarek/Nature-Inspired-Optimization-Algorithms/blob/main/Beluga%20Whales%20Optimization%20Code/Beluga%202.JPG" alt='Flowchart of the proposed BWO'>
</p>

<p align="center">
    <strong> Fig. 2 </strong> Flowchart of the proposed BWO. Source: https://www.researchgate.net/publication/361204761_Beluga_whale_optimization_A_novel_nature-inspired_metaheuristic_algorithm
</p>

## 8 fitness functions used in this optimization code.

1. Sphere function **F1**
2. Powell Sum function **F3**
3. schwefel 1.2 function **F4**
4. Rosenbrock function **F6**
5. Step function **F7**
6. Quartic funtion **F8**
7. Zakharov function **F9**
8. Rastrigin function **F13**

## How to try this code.

using command propmt in your machine type this command.
<code>python BWO.py fitness_function_arg max_iterations_arg number_of_whales_arg</code>

1. fitness_function_arg:- any value in **'F1', 'F3', 'F4', 'F6, 'F7', 'F8', 'F9', 'F13'** without **''**.
2. max_iterations_arg:- **INTEGER** value
3. number_of_whales_args:- **INTEGER** value

## Ref:-
<a target="_blank" href="https://www.researchgate.net/publication/361204761_Beluga_whale_optimization_A_novel_nature-inspired_metaheuristic_algorithm"><strong>Beluga whale optimization: A novel nature-inspired metaheuristic algorithm</strong></a>



