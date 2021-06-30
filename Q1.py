import random

class GLA(object):
    def __init__(self, graph, pop_size):
        self.neighbors , self.weights = graph
        self.pop_size = pop_size
        self.populations = []
        self.fitness_list = []
        self.optimal_result = 0
        self.prev_fitness = []
        for j in range(pop_size):
            population = []
            list_temp = [1, 2, 3, 4, 5, 6, 7]
            for i in range(len(self.weights)):
                node = random.choice(list_temp)
                if node in population:
                    for k in range(len(list_temp)):
                        if not(list_temp[k] in population):
                            population.append(list_temp[k])
                            node = list_temp[k]
                            break
                else:
                    population.append(node)
                list_temp = neighbors[node]
            if len(population) == len(self.weights):
                node = population[len(self.weights) - 1]
                list_temp = self.neighbors[node]
                if population[0] in list_temp:
                    population.append(population[0])
                    self.populations.append(population)
        print(self.populations)
        self.fitness()
        print(self.fitness_list)
        self.selection()
        print(self.populations)
        print(self.prev_fitness)

    def fitness(self):
        for i in range(len(self.populations)):
            prev = 0
            distance = 0
            for j in self.populations[i]:
                if prev != 0:
                    temp_list = self.neighbors[prev]
                    for k in range(len(temp_list)):
                        if temp_list[k] == j:
                            distance += self.weights[prev][k]
                            break

                prev = j
            if distance <= 63:
                self.optimal_result = self.populations[i]
            self.prev_fitness.append(distance)
            self.fitness_list.append(distance)

    def selection(self):  # using generation gap approach
        num_select = 6
        delete_num = len(self.populations) - num_select

        for i in range(delete_num):
            for j in range(len(self.prev_fitness)):
                max_value = max(self.prev_fitness)
                if self.prev_fitness[j] == max_value:
                    del self.prev_fitness[j]
                    del self.populations[j]
                    break

    def cross_over(self):
        pass

    def mutation(self):
        pass

    def plot(self):
        pass

if __name__ == "__main__":
    neighbors = {1: [2, 3, 7], 2:[1, 3, 4], 3:[1, 2, 4, 5, 7], 4:[2, 3, 5, 6], 5:[3, 4, 6, 7], 6:[4, 5, 7], 7:[1, 3, 5, 6]}
    weights = {1: [12, 10, 12], 2:[12, 8, 12], 3:[10, 8, 11, 3, 9], 4:[12, 11, 11, 10], 5:[3, 11, 6, 7], 6:[10, 6, 9], 7:[12, 9, 7, 9]}
    graph = (neighbors, weights)
    pop_size = 20
    gla = GLA(graph, pop_size)
    while gla.optimal_result == 0:
        gla.cross_over()
        break
    print("optimal result : ", gla.optimal_result)

