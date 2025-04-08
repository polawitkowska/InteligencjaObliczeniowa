import pygad
import numpy

weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
capacity = 25
best_value = 1630

gene_space = [0, 1]

def fitness_func(model, solution, solution_idx):
    total_weight = numpy.sum(solution * weights)
    total_value = numpy.sum(solution * values)
    
    if total_weight > capacity:
        return -1000 - (total_weight - capacity) * 100
    
    return total_value - abs(best_value - total_value) * 0.1

sol_per_pop = 10
num_genes = len(weights)

num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 8

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

selected_weight = numpy.sum(weights*solution)
selected_value = numpy.sum(values*solution)
print(f"Selected items total weight: {selected_weight}")
print(f"Selected items total value: {selected_value}")

ga_instance.plot_fitness()