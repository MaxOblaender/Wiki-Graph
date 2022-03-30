from turtle import width
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import graphClass

class Draw():
    my_graph = graphClass.Graph()
    nx_graph = nx.DiGraph()

    def __init__(self,graph):        
        self.my_graph = graph
        self.build_networkGraph()
        
    def build_networkGraph(self):
        for v in self.my_graph:
            self.nx_graph.add_node(v.get_label())
            for child in v.get_children():
                self.nx_graph.add_edge(v.get_label(),child.get_label())

    def draw(self):
        plt.figure(figsize=(40,40))

        # nx.draw_networkx(self.nx_graph, with_labels=True)
        # plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        # plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
        # for pos in ['right','top','bottom','left']:
        #     plt.gca().spines[pos].set_visible(False)

        requested_string = "" #input string
        # pos = nx.spring_layout(self.nx_graph)
        # pos = nx.circular_layout(self.nx_graph)
        # pos = nx.planar_layout(self.nx_graph)
        pos = nx.spiral_layout(self.nx_graph)
        color_map = ["red" if node == requested_string else "blue" for node in self.nx_graph]
        nx.draw(self.nx_graph,pos,width=2,edge_color='#BB0000',node_color=color_map,edge_cmap=plt.cm.Blues,with_labels=True)

        plt.show()



