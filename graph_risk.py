import networkx as nx

# Build topology graph
G = nx.DiGraph()
for node, attrs in nodes.items():
    G.add_node(node, **attrs)
for edge in edges:
    G.add_edge(edge["source"], edge["target"], **edge)

# Calculate critical nodes
betweenness = nx.betweenness_centrality(G)
print("Most critical node:", max(betweenness, key=betweenness.get))
