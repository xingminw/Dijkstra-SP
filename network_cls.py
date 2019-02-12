import numpy as np


class Network(object):
    def __init__(self, nodes_dict=None, origin_node=None,
                 dest_node=None, fixed_set=None, remaining_set=None):
        if nodes_dict is None:
            self.nodes = {}
        else:
            self.nodes = nodes_dict
        self.origin_node = origin_node
        self.dest_node = dest_node
        self.fixed_set = fixed_set
        self.remaining_set = remaining_set

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def initiate(self):
        self.fixed_set = [self.dest_node]
        self.nodes[self.dest_node].value_function = 0
        self.nodes[self.dest_node].best_path = [self.dest_node]

        for node_id in self.nodes.keys():
            if node_id in self.fixed_set:
                continue
            if self.remaining_set is None:
                self.remaining_set = []
            self.remaining_set.append(node_id)
        #
        # for node_id in self.remaining_set:
        #     node = self.nodes[node_id]
        #     if not (self.dest_node in node.dest_nodes.keys()):
        #         self.nodes[node_id].value_function = 100000
        #     else:
        #         self.nodes[node_id].value_function = node.dest_nodes[self.dest_node]
        #     self.nodes[node_id].best_path = [self.dest_node]

    def update(self):
        for node_id in self.remaining_set:
            node = self.nodes[node_id]
            node_candidate_dests = []
            node_candidate_values = []

            dest_nodes_id = node.dest_nodes
            for dest_id in dest_nodes_id:
                if not (dest_id in self.fixed_set):
                    continue
                node_candidate_dests.append(dest_id)
                node_candidate_values.append(node.dest_nodes[dest_id] +
                                             self.nodes[dest_id].value_function)

            if len(node_candidate_dests) == 0:
                continue

            min_dest_idx = int(np.argmin(node_candidate_values))
            minimum_value = node_candidate_values[min_dest_idx]
            best_dest_node = node_candidate_dests[min_dest_idx]

            self.nodes[node_id].value_function = minimum_value
            if self.nodes[node_id].best_path is None:
                self.nodes[node_id].best_path = []
            self.nodes[node_id].best_path = [best_dest_node] + self.nodes[node_id].best_path

        # select the new fixed node
        for node_id in self.remaining_set:
            node = self.nodes[node_id]


    def output_value_function(self):
        print("Fixed set", self.fixed_set)
        print("Remaining set", self.remaining_set)
        for node_id in self.nodes.keys():
            node = self.nodes[node_id]
            value_function = node.value_function
            best_path = node.best_path
            print("node id", node_id, ", value function", value_function, ", path", best_path)


class Node(object):
    def __init__(self, node_id, origin_nodes=None, dest_nodes=None,
                 value_function=None, best_path=None):
        self.node_id = node_id
        self.value_function = value_function
        self.best_path = best_path

        if origin_nodes is None:
            self.origin_nodes = {}
        else:
            self.origin_nodes = origin_nodes

        if dest_nodes is None:
            self.dest_nodes = {}
        else:
            self.dest_nodes = dest_nodes

