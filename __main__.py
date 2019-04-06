from graph import Graph

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")
graph.add_node("H")
graph.add_node("I")
graph.add_node("J")
graph.add_node("K")
graph.add_node("CB")

graph.add_edge("A", "B", 2)
graph.add_edge("B","I", 14)
graph.add_edge("B", "CB", 10)
graph.add_edge("B", "D", 8)
graph.add_edge("C", "D", 1)
graph.add_edge("C", "E", 1)
graph.add_edge("C", "CB", 10)
graph.add_edge("C", "G", 8)
graph.add_edge("D", "E", 1)
graph.add_edge("F", "G", 2)
graph.add_edge("F", "CB", 10)
graph.add_edge("F", "K", 13)
graph.add_edge("F", "H", 2)
graph.add_edge("G", "H", 2)
graph.add_edge("I", "K", 2)
graph.add_edge("I", "B", 14)
graph.add_edge("J", "CB", 10)
graph.add_edge("J", "K", 2)
graph.add_edge("J", "I", 2)
graph.add_edge("K", "F", 13)


start_node = input("Enter start node:")
end_node = input("Enter end node:")
print()


path_length, path = graph.find_shortest_path(start_node, end_node)

print(f"Total cost: {path_length}")


for i in range(len(path) - 1):
    print(f"{path[i].name} {path[i].neighbours_dict[path[i+1]]}-> ", end="")

print(path[-1].name)

