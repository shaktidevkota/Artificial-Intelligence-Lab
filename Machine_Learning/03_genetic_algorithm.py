# Question 3: Genetic Algorithm
# Shakti Raj Devkota

import random


def fitness(x):
    return -(x - 5) ** 2


def genetic_algorithm(population_size, generations, mutation_rate):
    population = [random.uniform(0, 10) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=fitness, reverse=True)

        # Selection
        parents = population[:population_size // 2]

        # Crossover
        new_population = parents[:]

        while len(new_population) < population_size:
            p1 = random.choice(parents)
            p2 = random.choice(parents)
            child = (p1 + p2) / 2

            # Mutation
            if random.random() < mutation_rate:
                child += random.uniform(-1, 1)

            child = max(0, min(10, child))
            new_population.append(child)

        population = new_population

    best = max(population, key=fitness)
    return best, fitness(best)


if __name__ == "__main__":
    n = int(input("Enter population size: "))
    g = int(input("Enter number of generations: "))
    m = float(input("Enter mutation rate: "))

    best, score = genetic_algorithm(n, g, m)

    print(f"\nBest solution: {best:.3f}")
    print(f"Fitness: {score:.3f}")