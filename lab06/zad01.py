import pygad
import numpy as np

# Dane wejściowe: wagi, wartości i maksymalna waga plecaka
weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
capacity = 25
num_items = len(weights)

def fitness_func(model, solution, solution_idx):
    total_weight = np.sum(np.array(weights) * solution)
    total_value = np.sum(np.array(values) * solution)
    
    if total_weight > capacity:
        fitness = -total_weight
    else:
        fitness = total_value
    return fitness

# Parametry algorytmu
ga_instance = pygad.GA(
    num_generations=100,
    num_parents_mating=5,
    fitness_func=fitness_func,
    sol_per_pop=20,
    num_genes=num_items,
    gene_type=int,
    init_range_low=0,
    init_range_high=2,  # geny: 0 lub 1
    mutation_type="random",
    mutation_percent_genes=10,
    parent_selection_type="rank"
)

# Uruchomienie algorytmu
ga_instance.run()

# Wyniki
solution, solution_fitness, solution_idx = ga_instance.best_solution()
total_weight = np.sum(np.array(weights) * solution)

print("Najlepsze rozwiązanie:", solution)
print("Wartość rozwiązania:", solution_fitness)
print("Waga rozwiązania:", total_weight)