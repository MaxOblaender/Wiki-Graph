from .graphClass import Graph
import networkx as nx
import matplotlib.pyplot as plt
import re

class Draw():
    """Klasse für die Darstellung des Graphen mit networkx"""
    my_graph = Graph() #der Graph aus meiner graphClass
    nx_graph = nx.DiGraph() #der Graph von networkx. Es ist nötig meinen Graphen zu übersetzen, da nx natürlich nur nx Graphen darstellen kann

    def __init__(self,graph,form,show):     
        """form entscheidet die Darstellungsart von nx und show den gesuchten String, falls angegeben"""   
        self.my_graph = graph
        
        self.build_networkGraph() 
        self.draw(form,show) 
        
    def build_networkGraph(self):
        """Übersetzt den Inputgraphen"""
        for node in self.my_graph:
            self.nx_graph.add_node(node.get_label()) #die nx nodes bekommen einfach das Label der Knoten aus meinem Graphen
            for child in node.get_children():
                self.nx_graph.add_edge(node.get_label(),child.get_label())

    def draw(self,form,request):
        """Zeigt dann den Graphen"""
        plt.figure(figsize=(40,40))
        if form == "spring": #die Verschiedenen Möglichkeiten der Darstellung.
            pos = nx.spring_layout(self.nx_graph)
        elif form == "spiral":
            pos = nx.spiral_layout(self.nx_graph)
        elif form == "planar":
            pos = nx.planar_layout(self.nx_graph)
        
        color_map = ["red" if re.search(request, node, re.IGNORECASE) else "mediumslateblue" for node in self.nx_graph] 
        # wenn der gesuchte string in einem Knoten gefunden wir, wird dieser roo, statt blau
        nx.draw(self.nx_graph,pos,width=2,edge_color='grey',node_color=color_map,edge_cmap=plt.cm.Blues,with_labels=True)

        plt.show()