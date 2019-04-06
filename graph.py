import sys

from node import Node

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

        dict_open = {}
        dict_open[start_node] = 0

        came_from = {}

        while len(dict_open) > 0:
            shortest_open = None
            shortest_open_distance = sys.maxsize
            for (node, distance) in dict_open.items():
                if distance < shortest_open_distance:
                    shortest_open_distance = distance
                    shortest_open = node

            assert shortest_open is not None

            del dict_open[shortest_open]

            if shortest_open is end_node:
                return (shortest_open_distance, self.reconstruct_path(came_from, start_node, end_node))

            for (neighbour, cost) in shortest_open.neighbours_dict.items():

                dict_open[neighbour] = shortest_open_distance + cost
                came_from[neighbour] = shortest_open

        return None

    def reconstruct_path(self, came_from, start_node, end_node):
        path = [end_node]

        while path[-1] is not start_node:
            path.append(came_from[path[-1]])

        path.reverse()

        return path



