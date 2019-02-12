import os
import network_cls


def load_network(file_name):
    with open(file_name, "r") as network_file:
        all_lines = network_file.readlines()

    network = network_cls.Network()

    for single_line in all_lines[1:]:
        if single_line[-1] == "\n":
            single_line = single_line[:-1]
        split_info = single_line.split(",")

        in_link_id = int(split_info[0])
        out_link_id = int(split_info[1])
        link_length = int(split_info[2])

        # create inlink node and outlink node
        if not (in_link_id in network.nodes.keys()):
            network.add_node(network_cls.Node(in_link_id))

        if not (out_link_id in network.nodes.keys()):
            network.add_node(network_cls.Node(out_link_id))

        network.nodes[in_link_id].dest_nodes[out_link_id] = link_length
        network.nodes[out_link_id].origin_nodes[in_link_id] = link_length
    return network


if __name__ == '__main__':
    load_network(os.path.join("input", "links.csv"))

