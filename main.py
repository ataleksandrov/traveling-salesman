import math
import numpy as np
import random


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        delta_x = abs(self.x - city.x)
        delta_y = abs(self.y - city.y)
        distance = math.sqrt((delta_x ** 2) + (delta_y ** 2))
        return distance


def create_random_route():
    route = np.random.permutation(len(cities))
    return route


class Individual:
    def __init__(self, route):
        self.route = route
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        fit = 0.0
        for i in range(0, len(self.route)):
            index = self.route[i]
            index2 = self.route[(i+1) % len(self.route)]
            fit += cities[index].distance(cities[index2])
        return 1 / fit

    def mutate(self):
        for i in range(0, len(self.route) - 1):
            if random.random() % 1 < 0.015:
                self.route[i] = self.route[i + 1]


def create_individual(parent1, parent2):
    child = []
    for i in range(0, math.ceil(len(parent1.route) / 2)):
        child.append(parent1.route[i])

    for gen in parent2.route:
        if gen not in child:
            child.append(gen)
    return Individual(child)


cities = []
for j in range(0, 25):
    cities.append(City(x=int(random.random()*500), y=int(random.random()*500)))


def new_population(pop_size):
    population = []
    for i in range(0, pop_size):
        population.append(Individual(create_random_route()))
    return population


def crossover(best_individuals):
    children = []
    while len(children) < 100 - len(best_individuals):
        index = random.randint(0, len(best_individuals)-1)
        index2 = (index + random.randint(0, len(best_individuals)-1)) % len(best_individuals)
        children.append(create_individual(best_individuals[index], best_individuals[index2]))

    return children


def genetic_algorithm(generations):
    population = new_population(100)
    population.sort(key=lambda ind: ind.fitness, reverse=True)
    print(population[0].fitness)

    for g in range(0, generations):
        population.sort(key=lambda ind: ind.fitness, reverse=True)

        if g in [10, 50, 100]:
            print(population[0].fitness)

        best_individuals = population[:60]
        children = crossover(best_individuals)
        for k in range(0, len(children)):
            children[k].mutate()
        best_individuals.extend(children)
        population = best_individuals

    print(population[0].fitness)


def main():
    genetic_algorithm(300)


if __name__ == "__main__":
    main()
