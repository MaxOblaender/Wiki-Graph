from .graphClass import Graph
import networkx as nx
import matplotlib.pyplot as plt
import re


class Draw():
    my_graph = Graph()
    nx_graph = nx.DiGraph()

    def __init__(self,graph,form,show):        
        self.my_graph = graph
        
        self.build_networkGraph()
        self.draw(form,show)
        
    def build_networkGraph(self):
        for node in self.my_graph:
            self.nx_graph.add_node(node.get_label())
            for child in node.get_children():
                self.nx_graph.add_edge(node.get_label(),child.get_label())

    def draw(self,form,request):
        plt.figure(figsize=(40,40))
        if form == "spring":
            pos = nx.spring_layout(self.nx_graph)
        elif form == "spiral":
            pos = nx.spiral_layout(self.nx_graph)
        elif form == "planar":
            pos = nx.planar_layout(self.nx_graph)
        
        color_map = ["red" if re.search(request, node, re.IGNORECASE) else "mediumslateblue" for node in self.nx_graph]
        nx.draw(self.nx_graph,pos,width=2,edge_color='grey',node_color=color_map,edge_cmap=plt.cm.Blues,with_labels=True)

        plt.show()



# nx.draw_networkx(self.nx_graph, with_labels=True)
        # plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        # plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
        # for pos in ['right','top','bottom','left']:
        #     plt.gca().spines[pos].set_visible(False)

        # requested_string = request

        # pos = nx.spring_layout(self.nx_graph)
        # pos = nx.circular_layout(self.nx_graph) # macht kein Sinn
        # pos = nx.planar_layout(self.nx_graph)
        # pos = nx.spiral_layout(self.nx_graph)