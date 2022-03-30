
from numpy import empty


class Vertex():
    """Klasse um die Vertices des Graphen darzustellen"""

    def __init__(self, label):
        """Konstruktor setzt den Seitennamen als label"""
        self.label = label
        self.children = set() #gerichtet ist hier immer von sich selbst zu adjacent
        self.parents = set()

    #def __str__(self):
     #   return str(self.label) + "adjacent:" + str([v.label for v in self.adjacent])

    def add_child(self,child): #fügt Kante von sich selbst zum Nachbarn hin hinzu
        """Fühgt eine Kante zu einem gegebenen Vertex hinzu"""
        self.children.add(child)
    
    def add_parent(self,parent):
        self.parents.add(parent)

    def get_children(self):
        return self.children

    def get_parents(self):
        """Gibt alle verbundenen Vertices von diesem Vertex zurück"""
        return self.parents

    def get_label(self):
        return self.label

class Graph():
    """Klasse die den Graphen darstellt"""

    def __init__(self):
        """Konstruktor. Vertices werden in einem Dictionary gespeichert"""
        self.vertices_dict = {}
        self.num_vertices = 0
        self.num_edges = 0

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def add_vertex(self,label):
        """Fügt neuen Vertex ein. Setzt keine Kanten"""
        if not label in self.vertices_dict:
            self.num_vertices = self.num_vertices +1
            new_vertex = Vertex(label) #muss prüfen, ob es schon einen Vertex mit dem Label gibt (macht das ein dict schon? ja ne?)
            self.vertices_dict[label] = new_vertex
            print(label)
        else:
            print(label," was already found!")

    def get_vertex(self,label):
        """Holt den Vertix mit dem gesuchten Seitennamen aus dem Dictionary"""
        if(label in self.vertices_dict):
            return self.vertices_dict[label]
        else:
            pass #vielleicht noch abfangen

    def add_edge(self,label_parent,label_child):
        """Fügt Kante zwischen label und label_end über eine Vertex-Methode ein."""
        if(label_parent and label_child in self.vertices_dict):
            self.vertices_dict[label_parent].add_child(self.vertices_dict[label_child])
            self.vertices_dict[label_child].add_parent(self.vertices_dict[label_parent])
            self.num_edges = self.num_edges + 1

    def get_neighbours(self,vertex): #was wenn gleichzeitig parent und child??
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
        E = self.num_edges
        V = self.num_vertices
        return E/(V*(V-1))

    def __str__(self): #nicht wirklich richtig
        output = ""
        counter = 0

        for label in self.vertices_dict: 
            if self.vertices_dict[label].get_children():
                output = output + label
                counter +=1
                output = output + "\n"
            for child in self.vertices_dict[label].get_children():
                output = output + "\t" + child.get_label() + " \n"
                counter +=1
        return str(output)

