from pyvis.network import Network

from dfs import DFS
from graph import graph, vertex, stack

net = Network()

for node in graph:
    net.add_node(node, str(node))

DFS(graph, vertex, stack, net)

net.show("graph.html", notebook=False)