from node import Node
from priority import PriorityQueue

from typing import Dict, List, Optional, Tuple
import sys

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}

    def add_node(self, name: str) -> None:
        self.nodes[name] = Node(name)

    def add_edge(self, node1_name: str, node2_name: str, cost: int) -> None:
        node1 = self.nodes[node1_name]
        node2 = self.nodes[node2_name]
        node1.add_neighbour(node2, cost)
        node2.add_neighbour(node1, cost)

    def find_shortest_path(self, start_node_name: str, end_node_name: str) -> Optional[Tuple[int, List[Node]]]:
        start_node = self.nodes[start_node_name]
        end_node = self.nodes[end_node_name]

        open_nodes = {}
        open_nodes[start_node] = 0

        closed = set()

        came_from = {}

        while len(open_nodes) > 0:
            shortest_node = min(open_nodes, key=open_nodes.get)
            shortest_node_distance = open_nodes[shortest_node]
            del open_nodes[shortest_node]
            closed.add(shortest_node)

            if shortest_node is end_node:
                return shortest_node_distance, self.reconstruct_path(came_from, start_node, end_node)

            for (neighbour, cost) in shortest_node.neighbours_dict.items():
                if neighbour in closed:
                    continue
                minimum_known_cost = open_nodes.get(neighbour, sys.maxsize)
                current_cost = shortest_node_distance + cost

                if current_cost < minimum_known_cost:
                    open_nodes[neighbour] = current_cost
                    came_from[neighbour] = shortest_node

        return None

    def reconstruct_path(self, came_from: Dict[Node, Node], start_node: Node, end_node: Node) -> List[Node]:
        path = [end_node]

        while path[-1] is not start_node:
            path.append(came_from[path[-1]])

        path.reverse()

        return path



