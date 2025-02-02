#!/usr/bin/env python
# coding: utf-8

import math
import random

# Definition of the Sphere function
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    current_value = func(current)
    step_size = 0.1
    
    for _ in range(iterations):
        neighbor = [max(bounds[i][0], min(bounds[i][1], current[i] + random.uniform(-step_size, step_size))) for i in range(dim)]
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value
        
        if abs(neighbor_value - current_value) < epsilon:
            break
    
    return current, current_value

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    best_value = func(best)
    
    for _ in range(iterations):
        candidate = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
        candidate_value = func(candidate)
        
        if candidate_value < best_value:
            best, best_value = candidate, candidate_value
        
        if abs(candidate_value - best_value) < epsilon:
            break
    
    return best, best_value

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    current_value = func(current)
    
    for _ in range(iterations):
        temp *= cooling_rate
        neighbor = [max(bounds[i][0], min(bounds[i][1], current[i] + random.uniform(-1, 1))) for i in range(dim)]
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value or math.exp((current_value - neighbor_value) / temp) > random.random():
            current, current_value = neighbor, neighbor_value
        
        if temp < epsilon:
            break
    
    return current, current_value

# Main
if __name__ == "__main__":
    # Boundaries for the function
    bounds = [(-5, 5), (-5, 5)]
    
    # Execution of algorithms
    print("[*] Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Solution:", hc_solution, "\nValue:", hc_value)
    
    print("\n[*] Random Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Solution:", rls_solution, "\nValue:", rls_value)
    
    print("\n[*] Simulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Solution:", sa_solution, "\nValue:", sa_value)
