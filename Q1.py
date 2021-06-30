import random
import numpy as np

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
        print("first population : ", self.populations)
        self.fitness()
        print("fitness list : ", self.fitness_list)
        self.selection()
        print("selected population : ", self.populations)
        print("fitness : ", self.prev_fitness)
        self.mutation(self.populations)

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

    def mutation(self, old_populations):
        flag_list = np.zeros(len(old_populations))
        new_population = []
        count = 0
        for p in old_populations:
            for i in range(1, len(p) - 2):
                prev = p[i - 1]
                subsequence = p[i + 2]
                if (prev in self.neighbors[p[i]]) and (subsequence in self.neighbors[p[i]]):
                    if (prev in self.neighbors[p[i + 1]]) and (subsequence in self.neighbors[p[i + 1]]):
                        p = self.swap(p, i, i + 1)
                        new_population.append(p)
                        flag_list[count] += 1
                        break
            count += 1

        print("new population : ", new_population)
        print("change flag : ", flag_list)
        return new_population

    def swap(self, p_list, pos1, pos2):
        temp = p_list[pos1]
        p_list[pos1] = p_list[pos2]
        p_list[pos2] = temp
        return p_list

    def plot(self):
        pass

if __name__ == "__main__":
    neighbors = {1: [2, 3, 7], 2:[1, 3, 4], 3:[1, 2, 4, 5, 7], 4:[2, 3, 5, 6], 5:[3, 4, 6, 7], 6:[4, 5, 7], 7:[1, 3, 5, 6]}
    weights = {1: [12, 10, 12], 2:[12, 8, 12], 3:[10, 8, 11, 3, 9], 4:[12, 11, 11, 10], 5:[3, 11, 6, 7], 6:[10, 6, 9], 7:[12, 9, 7, 9]}
    graph = (neighbors, weights)
    pop_size = 20
    gla = GLA(graph, pop_size)
    while gla.optimal_result == 0:
        # gla.populations = gla.mutation(gla.populations)
        print("while : ")
        break
    print("optimal result : ", gla.optimal_result)

