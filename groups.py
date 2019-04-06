from graph import Graph

import itertools

class Group:
    def __init__(self, nodes, sender_nodes, internal_cost):
        self.sender_nodes = sender_nodes
        self.nodes = nodes
        self.internal_cost = internal_cost

class Groups:
    def __init__(self):
        self.groups = {}
        self.graph = Graph()

    def add_group(self, name, nodes, sender_nodes, internal_cost):
        nodes = [self.node_name(name, node) for node in nodes]
        sender_nodes = [self.node_name(name, node) for node in sender_nodes]
        self.groups[name] = Group(nodes, sender_nodes, internal_cost)

        for node in nodes:
            self.graph.add_node(node)
        for sender_node in sender_nodes:
            self.graph.add_node(sender_node)

        for (node1, node2) in itertools.combinations(sender_nodes, 2):
            self.graph.add_edge(node1, node2, internal_cost)


    def add_inter_group_connection(self, group1, sender1, group2, sender2, cost):
        self.graph.add_edge(f"{group1}-{sender1}", f"{group2}-{sender2}", cost)

    def find_path(self, start_group_name, start_node, end_group_name, end_node):
        start_name = self.node_name(start_group_name, start_node)
        end_name = self.node_name(end_group_name, end_node)

        start_group = self.groups[start_group_name]
        end_group = self.groups[end_group_name]

        if start_group is end_group:
            return start_group.internal_cost, [self.graph.nodes[start_name], self.graph.nodes[end_name]]

        if start_name not in start_group.sender_nodes:
            for sender_node in start_group.sender_nodes:
                self.graph.add_edge(start_name, sender_node, start_group.internal_cost)
        if end_name not in end_group.sender_nodes:
            for sender_node in end_group.sender_nodes:
                self.graph.add_edge(end_name, sender_node, end_group.internal_cost)

        return self.graph.find_shortest_path(start_name, end_name)



    def node_name(self, group, name):
        return f"{group}-{name}"
