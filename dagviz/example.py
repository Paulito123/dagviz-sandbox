from dagviz import render_svg
import networkx as nx

# Create the DAG
G = nx.DiGraph()
for i in range(6):
    G.add_node(f"n{i}")
    
G.add_edge(f"n0", f"n1")
G.add_edge(f"n0", f"n2")
G.add_edge(f"n0", f"n4")
G.add_edge(f"n1", f"n3")
G.add_edge(f"n2", f"n3")
G.add_edge(f"n3", f"n4")
G.add_edge(f"n0", f"n5")
G.add_edge(f"n1", f"n5")
G.add_edge(f"n2", f"n5")
G.add_edge(f"n3", f"n5")

# Create an SVG as a string
r = render_svg(G)
with open("output/dagviz.svg", "wt") as fs:
    fs.write(r)
    