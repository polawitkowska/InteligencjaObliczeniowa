import pygad

labirynth = [
    [0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0]
]
max_moves = 30
gene_space = [0, 1, 2, 3]

def fitness_func(model, solution, solution_idx):
    start_x, start_y = 0, 0
    end_x, end_y = len(labirynth)-1, len(labirynth[0])-1
    current_x, current_y = start_x, start_y
    moves = 0

    visited = set()
    visited.add((current_x, current_y))

    for move in solution:
        prev_x, prev_y = current_x, current_y
        
        if move == 0:  # góra
            if current_x > 0 and labirynth[current_x-1][current_y] != 1:
                current_x -= 1
        elif move == 1:  # prawo
            if current_y < len(labirynth[0])-1 and labirynth[current_x][current_y+1] != 1:
                current_y += 1
        elif move == 2: # dół
            if current_x < len(labirynth[0])-1 and labirynth[current_x+1][current_y] != 1:
                current_x += 1
        elif move == 3: # lewo
            if current_y > 0 and labirynth[current_x][current_y-1] != 1:
                current_y -= 1

        if (current_x, current_y) != (prev_x, prev_y) and (current_x, current_y) not in visited:
            moves += 1
            visited.add((current_x, current_y))
        elif (current_x, current_y) in visited:
            current_x, current_y = prev_x, prev_y

    distance = abs(current_x - end_x) + abs(current_y - end_y)

    if distance == 0:
        return moves
    else:
        return -distance
    

num_genes = 18
sol_per_pop = 200
num_generations = 500
mutation_percent_genes = 10
num_parents_mating = 20
keep_parents = 2

parent_selection_type = "tournament"
crossover_type = "two_points"

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

