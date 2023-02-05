<h1 align='center'>Nature-Inspired-Optimization-Algorithms</h1>
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
  <img src="https://github.com/Eng-ZeyadTarek/Nature-Inspired-Optimization-Algorithms/blob/main/Beluga%201.JPG" alt='Behaviors of beluga whales'>
</p>

<p align="center">
    Fig. 1 Behaviors of beluga whales, (a) swim, corresponding to exploration phase; (b) foraging, corresponding to exploitation phase, (c) whale fall, for whale fall phase. Source: https://constative.com/animals/whale-watching, https://www.sealuxe.ca/blog/narwhal
</p>

