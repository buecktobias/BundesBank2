from node import Node
from priority import PriorityQueue

class Graph:
    def __init__(self):
        self.dict_nodes = {}  # name and node class

    def add_node(self, name):
        self.dict_nodes[name] = Node(name)

    def add_edge(self, node1_name, node2_name, cost):
        node1 = self.dict_nodes[node1_name]
        node2 = self.dict_nodes[node2_name]
        node1.add_neighbour(node2, cost)
        node2.add_neighbour(node1, cost)

    def find_shortest_path(self, start_node_name, end_node_name):
        start_node = self.dict_nodes[start_node_name]
        end_node = self.dict_nodes[end_node_name]

        open = PriorityQueue()
        open.push(start_node, 0)

        came_from = {}

        while len(open) > 0:
            shortest_open, shortest_open_distance = open.pop()

            if shortest_open is end_node:
                return shortest_open_distance, self.reconstruct_path(came_from, start_node, end_node)

            for (neighbour, cost) in shortest_open.neighbours_dict.items():
                if neighbour in came_from:
                    continue
                open.push(neighbour, shortest_open_distance + cost)
                came_from[neighbour] = shortest_open

        return None

    def reconstruct_path(self, came_from, start_node, end_node):
        path = [end_node]

        while path[-1] is not start_node:
            path.append(came_from[path[-1]])

        path.reverse()

        return path



