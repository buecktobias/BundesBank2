from groups import Groups

groups = Groups()

groups.add_group("1", ["A", "B", "C", "D", "E"], ["D", "E"], 1)
groups.add_group("2", ["A", "B", "C"], ["D"], 1)
groups.add_group("3", ["A", "B", "C"], ["D"], 1)

groups.add_inter_group_connection("1", "D", "2", "D", 7)
groups.add_inter_group_connection("1", "E", "3", "D", 7)


start_node_group = input("Enter start node group:")
start_node = input("Enter start node:")
end_node_group = input("Enter end node group:")
end_node = input("Enter end node:")
print()


path_length, path = groups.find_path(start_node_group, start_node, end_node_group, end_node)

print(f"Total cost: {path_length}")


for i in range(len(path) - 1):
    print(f"{path[i].name} {path[i].neighbours_dict[path[i+1]]}-> ", end="")

print(path[-1].name)

