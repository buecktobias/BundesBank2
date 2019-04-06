from graph import Graph

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")

graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 1)
graph.add_edge("A", "C", 3)


path_length, path = graph.find_shortest_path("A", "C")
print(path_length)
print([node.name for node in path])
