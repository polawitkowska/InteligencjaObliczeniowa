import matplotlib.pyplot as plt
import random
from aco import AntColony
import random

plt.style.use("dark_background")

COORDS = [
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (30, 21),
    (20, 42),
    (1, 48),
    (27, 43),
    (20, 19),
    (10, 21),
    (30, 50),
    (3, 5),
    (87, 30),
    (65, 40),
    (16, 21),
    (33, 15),
    (22, 11),
    (20, 31),
    (18, 49),
    (44, 30),
    (2, 6),
    (76, 76),
    (56, 12),
    (61, 32),
    (8, 18),
    (19, 8),
    (16, 20),
    (48, 31),
    (49, 49),
    (2, 19)
]

def random_coord():
    r = random.randint(0, len(COORDS))
    return r

def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])

def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))

plot_nodes()

colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2, 
                    pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                    iterations=300) #wzrost mrówek spowalnia program, ale daje lepsze wyniki
# wzrost alpha i beta przyspiesza program ale zmniejsza dokładność

optimal_nodes = colony.get_path()

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )

plt.show()