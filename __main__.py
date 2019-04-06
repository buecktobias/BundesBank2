from graph import Graph

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

graph.add_edge("A", "B", 2)
graph.add_edge("D", "E", 1)
graph.add_edge("D", "C", 1)
graph.add_edge("E", "C", 1)
graph.add_edge("E", "D", 1)
graph.add_edge("C", "CB", 10)
graph.add_edge("B", "CB", 10)
graph.add_edge("B", "I", 14)
graph.add_edge("C", "G", 8)



path_length, path = graph.find_shortest_path("A", "C")
print(path_length)
print([node.name for node in path])
