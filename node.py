class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbours_dict = {}

    def add_neighbour(self, node: 'Node', cost: int) -> None:
        self.neighbours_dict[node] = cost
