
class Vertex():
    """Klasse um die Vertices des Graphen darzustellen"""

    def __init__(self, label):
        """Konstruktor setzt den Seitennamen als label. Die Nachfolger/Vorgänger sind Mengen."""
        self.label = label
        self.children = set() 
        self.parents = set()

    def add_child(self,child): 
        """Fühgt eine Kante zu einem gegebenen Nachfolger hinzu"""
        self.children.add(child)
    
    def add_parent(self,parent):
        """Fühgt eine Kante zu einem gegebenen Vorgänger hinzu"""
        self.parents.add(parent)

    def get_children(self):
        return self.children

    def get_parents(self):        
        return self.parents

    def get_label(self):
        return self.label

class Graph():
    """Klasse die den Graphen darstellt"""

    def __init__(self):
        """Vertices werden in einem Dictionary gespeichert, mit dem Seitennamen als Key und dem Knoten Objekt als Value"""
        self.vertices_dict = {}
        self.num_vertices = 0
        self.num_edges = 0

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def add_vertex(self,label):
        """Fügt neuen Vertex ein. Setzt keine Kanten"""
        if not (label in self.vertices_dict): # Prüft ob die Seite bereits gefunden wurde
            self.num_vertices = self.num_vertices +1
            new_vertex = Vertex(label) 
            self.vertices_dict[label] = new_vertex

    def get_vertex(self,label):
        """Holt den Vertix mit dem gesuchten Seitennamen aus dem Dictionary"""
        if(label in self.vertices_dict):
            return self.vertices_dict[label]
        else:
            raise KeyError("Site not found in graph!")

    def add_edge(self,label_parent,label_child):
        """Fügt Kante zwischen label_parent und label_child über eine Vertex-Methode ein."""
        if((label_parent and label_child) in self.vertices_dict):
            self.vertices_dict[label_parent].add_child(self.vertices_dict[label_child])
            self.vertices_dict[label_child].add_parent(self.vertices_dict[label_parent])
            self.num_edges = self.num_edges + 1

    def get_neighbours(self,vertex):
        """Abfragen alle Nachbarknoten"""
        neighbors = set()
        for parent in vertex.get_parents():
            neighbors.add(parent)
        for child in vertex.get_children():
            neighbors.add(child)
        return neighbors

    def get_highest_entry_degree(self):
        """Abfrage des Knotens mit den meisten Eltern"""
        highest_vertex = None
        number = 0
        for vertex in self.vertices_dict:
            amount = len(vertex.get_parents())
            if amount > number:
                highest_vertex = vertex
        return highest_vertex

    def get_highest_exit_degree(self):
        """Abfrage des Knotens mit den meisten Kindern"""
        highest_vertex = None
        number = 0
        for vertex in self.vertices_dict:
            amount = len(vertex.get_children())
            if amount > number:
                highest_vertex = vertex
        return highest_vertex

    def get_density(self):
        """Berechnet die Dichte des Graphen"""
        E = self.num_edges
        V = self.num_vertices
        return E/(V*(V-1))

    def __str__(self):
        """Methode um den Graphen als String darzustellen und auszugeben. 
        Schreibt den Eltern Knoten und dann eingerückt die Kinder"""
        output = ""
        counter = 0

        for label in self.vertices_dict: 
            if self.vertices_dict[label].get_children():
                output = output + label
                counter +=1
                output = output + "\n"
            for child in self.vertices_dict[label].get_children():
                output = output + "\t" + child.get_label() + "\n"
                counter +=1
        return output

