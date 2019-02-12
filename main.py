import os
from load_network import load_network


network = load_network(os.path.join("input", "links.csv"))
network.dest_node = 5

# initiate
network.initiate()
network.update()

network.output_value_function()
