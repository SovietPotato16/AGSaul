from functools import partial
from problems import knapsack
from algorithms import bruteforce, genetic
from utils.analyze import timer


things = knapsack.generate_things(22)
things = knapsack.second_example

weight_limit = 6500

print("Peso Limite: %dkg" % weight_limit)
print("")
print("Fuerza Bruta")
print("----------")

with timer():
	result = bruteforce(things, weight_limit)

knapsack.print_stats(result[1])

print("")
print("Algoritmo Genetico")
print("----------")

with timer():
	population, generations = genetic.run_evolution(
		populate_func=partial(genetic.generate_population, size=10, genome_length=len(things)),
		fitness_func=partial(knapsack.fitness, things=things, weight_limit=weight_limit),
		fitness_limit=result[0],
		generation_limit=100
	)

def print_stats(population: Population, generation_id: int, fitness_func: FitnessFunc):
    print("Generacion %02d" % generation_id)
    print("=============")
    print("Poblacion: [%s]" % ", ".join([genome_to_string(gene) for gene in population]))
    print("Promedio: %f" % (population_fitness(population, fitness_func) / len(population)))
    sorted_population = sort_population(population, fitness_func)
    print(
        "Mejor: %s (%f)" % (genome_to_string(sorted_population[0]), fitness_func(sorted_population[0])))
    print("Peor: %s (%f)" % (genome_to_string(sorted_population[-1]),
                              fitness_func(sorted_population[-1])))
    print("")
    xpoints = np.array([population_fitness(population, fitness_func),genome])
	ypoints = np.array([0, sorted_population])
	plt.plot(xpoints, ypoints)
	plt.show()
    
    matplotlib.rcParams['Gemeracion']

    return sorted_population[0]



sack = knapsack.from_genome(population[0], things)

knapsack.print_stats(sack)

