class Vertex():
    """Klasse um die Vertices des Graphen darzustellen"""

    def __init__(self, label):
        """Konstruktor setzt den Seitennamen als label"""
        self.label = label
        self.adjacent = set()

    #def __str__(self):
     #   return str(self.label) + "adjacent:" + str([v.label for v in self.adjacent])

    def add_adjacent(self,neighbour):
        """Fühgt eine Kante zu einem gegebenen Vertex hinzu"""
        if(neighbour in self.adjacent):
            #noch schauen, ob neighbour schon in set
            return False
        else:
            self.adjacent.add(neighbour)
            return True

    def get_label(self):
        return self.label

    def get_adjacent(self):
        """Gibt alle verbundenen Vertices von diesem Vertex zurück"""
        return self.adjacent

class Graph():
    """Klasse die den Graphen darstellt"""

    def __init__(self):
        """Konstruktor. Vertices werden in einem Dictionary gespeichert"""
        self.vertices_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def add_vertex(self,label):
        """Fügt neues Vertex ein. Setzt keine Kanten"""
        new_vertex = Vertex(label)
        self.num_vertices = self.num_vertices +1
        self.vertices_dict[label] = new_vertex
        #return new_vertex

    def get_vertex(self,label):
        """Holt den Vertice mit dem gesuchten Seitennamen aus dem Dictionary"""
        if(label in self.vertices_dict):
            return self.vertices_dict[label]
        else:
            pass #vielleicht noch abfangen

    def add_edge(self,label,label_end):
        if(label and label_end in self.vertices_dict):
            self.vertices_dict[label].add_adjacent(self.vertices_dict[label_end])
            #self.vertices_dict[label_end].add_neighbour(self.vertices_dict[label_start])
