import random

class GLA(object):
    def __init__(self, graph, pop_size):
        self.neighbors , self.weights = graph
        self.pop_size = pop_size
        self.populations = []
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

            self.populations.append(population)
        print(self.populations)

    def selection(self):
        pass

    def cross_over(self):
        pass

    def mutation(self):
        pass

if __name__ == "__main__":
    neighbors = {1: [2, 3, 7], 2:[1, 3, 4], 3:[1, 2, 4, 5, 7], 4:[2, 3, 5, 6], 5:[3, 4, 6, 7], 6:[4, 5, 7], 7:[1, 3, 5, 6]}
    weights = {1: [12, 10, 12], 2:[12, 8, 12], 3:[10, 8, 11, 3, 9], 4:[12, 11, 11, 10], 5:[3, 11, 6, 7], 6:[10, 6, 9], 7:[12, 9, 7, 9]}
    graph = (neighbors, weights)
    pop_size = 8
    gla = GLA(graph, pop_size)

