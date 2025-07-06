import random

BOARD_SIZE = 8
NUM_QUEENS = 8


def generate_population(size):
    population = []
    for _ in range(size):
        individual = random.sample(range(BOARD_SIZE), NUM_QUEENS)
        population.append(individual)
    return population


def calculate_fitness(individual):
    attacks = 0
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == j - i:
                attacks += 1
    return 1 / (attacks + 1)


def tournament_selection(population, k=3):
    selected = []
    for _ in range(len(population)):
        participants = random.sample(population, k)
        winner = max(participants, key=lambda x: calculate_fitness(x))
        selected.append(winner)
    return selected


def crossover(parent1, parent2):
    crossover_point = random.randint(1, NUM_QUEENS - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutation(individual, mutation_rate):
    if random.random() < mutation_rate:
        index = random.randint(0, NUM_QUEENS - 1)
        individual[index] = random.randint(0, BOARD_SIZE - 1)
    return individual


def genetic_algorithm(population_size, mutation_rate, generations):
    population = generate_population(population_size)
    for _ in range(generations):
        population = tournament_selection(population)
        next_generation = []
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            next_generation.extend([child1, child2])
        population = next_generation
    return max(population, key=lambda x: calculate_fitness(x))


solution = genetic_algorithm(population_size=100, mutation_rate=0.1, generations=1000)
print("Solution:", solution)
