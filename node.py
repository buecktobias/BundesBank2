class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours_dict = {}

    def add_neighbour(self, node, cost):
        self.neighbours_dict[node] = cost
