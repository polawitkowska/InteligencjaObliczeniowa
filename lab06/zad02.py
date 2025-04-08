import pygad
import math

def endurance(x, y, z, u, v, w):
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

gene_space = {'low': 0, 'high': 1}

def fitness_func(model, solution, solution_idx):
    x, y, z, u, v, w = solution
    endurance_value = endurance(x, y, z, u, v, w)
    return endurance_value
    

num_genes = 6
sol_per_pop = 50
num_generations = 200

parent_selection_type = "tournament"
crossover_type = "two_points"
mutation_percent_genes = 15

num_parents_mating = 5
keep_parents = 2

ga_instance = pygad.GA(gene_space=gene_space,
                    num_generations=num_generations,
                    num_parents_mating=num_parents_mating,
                    fitness_func=fitness_func,
                    sol_per_pop=sol_per_pop,
                    num_genes=num_genes,
                    parent_selection_type=parent_selection_type,
                    keep_parents=keep_parents,
                    crossover_type=crossover_type,
                    mutation_type="random",
                    mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
ga_instance.plot_fitness()

"""
Parameters of the best solution : [0.11647328 0.11617222 0.99747224 0.99978212 0.00439268 0.01817104]
Fitness value of the best solution = 2.839984628572151
"""