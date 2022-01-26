class Vertex():
    """Klasse um die Vertices des Graphen darzustellen"""

    def __init__(self, lable):
        """Konstruktor setzt den Seitennamen als label"""
        self.lable = lable
        self.children = set()

    def add_neighbour(self,neighbour):
        """Fühgt eine Kante zu einem gegebenen Vertex hinzu"""
        self.children.add(neighbour)

    def get_lable(self):
        return self.lable

    def get_children(self):
        """Gibt alle verbundenen Vertices von diesem Vertex zurück"""
        return self.children

class Graph():
    """Klasse die den Graphen darstellt"""

    def __init__(self):
        """Konstruktor. Vertices werden in einem Dictionary gespeichert"""
        self.vertices_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def add_vertex(self,lable):
        """Fügt neues Vertex ein. Setzt keine Kanten"""
        new_vertex = Vertex(lable)
        self.num_vertices = self.num_vertices +1
        self.vertices_dict[lable] = new_vertex
        #return new_vertex

    def get_vertex(self,lable):
        """Holt den Vertice mit dem gesuchten Seitennamen aus dem Dictionary"""
        if(lable in self.vertices_dict):
            return self.vertices_dict[lable]
        else:
            pass #vielleicht noch abfangen

    def add_edge(self,lable_start,lable_end):
        if(lable_start and lable_end in self.vertices_dict):
            self.vertices_dict[lable_start].add_neighbour(self.vertices_dict[lable_end])
            #self.vertices_dict[lable_end].add_neighbour(self.vertices_dict[lable_start])

if __name__ == "__main__":

    g = Graph()

    g.add_vertex("test1")
    g.add_vertex("test2")
    g.add_vertex("test3")

    g.add_edge("test2","test3")
    g.add_edge("test1","test2")


    for v in g:
        print("lable:"+v.lable)
        for c in v.get_children():
            print("parent:",v.get_lable(),"child:",c.get_lable())