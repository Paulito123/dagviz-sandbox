from graphviz import Digraph
import networkx as nx

# Create the DAG
dot = Digraph()

dot.node('A', 'Start')    
dot.node('B', 'Process')
dot.node('C', 'End')
dot.edges(['AB', 'AC', 'BC'])

# Create an SVG as a string
dot.render('output/test.gv', view=True)
    