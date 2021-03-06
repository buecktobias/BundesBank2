from groups import Groups

groups = Groups()

groups.add_group("1", ["A"], ["B"], 2)
groups.add_group("2", ["E"], ["C", "D"], 1)
groups.add_group("3", ["H"], ["F", "G"], 2)
groups.add_group("4", [], ["I", "J", "K"], 2)
groups.add_group("CB", [], ["CB"], 0)

groups.add_inter_group_connection("1", "B", "2", "D", 8)
groups.add_inter_group_connection("1", "B", "4", "J", 14)
groups.add_inter_group_connection("2", "C", "3", "G", 8)
groups.add_inter_group_connection("3", "F", "4", "K", 13)

groups.add_inter_group_connection("CB", "CB", "1", "B", 10)
groups.add_inter_group_connection("CB", "CB", "2", "C", 10)
groups.add_inter_group_connection("CB", "CB", "3", "F", 10)
groups.add_inter_group_connection("CB", "CB", "4", "J", 10)


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

