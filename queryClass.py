import graphClass
import requests
import re

class Query():
    """Klasse zum holen und verarbeiten der HTML-Seiten"""
    g = graphClass.Graph
    def __init__(self,graph):           
        self.g = graph
        self.first = True

    def find_titel(self,url):
        """Setzt den titel(label)"""
        self.HTML = requests.get(url).text
        tmp_title_list = re.findall("<title>.*-",self.HTML)
        try:    #falls kein Titel gefunden werden kann
            tmp_title = tmp_title_list[0] 
        except:
            print("no titel--------------------------------------------------------------")
            return
        tmp_title = re.sub("<title>","",tmp_title)
        return re.sub("\s-","",tmp_title)       

    def find_all_links(self,url,last_label,depth):
        #findet alle "a href" und setzt eigenen titel
        self.HTML = requests.get(url).text 
        

        #es soll sich last_label nur ändern, wenn depth sich geändert hat
        #bzw. last_rekusion_level
        

        
        self.label = self.find_titel(url)

        


        # g.add_vertex(self.label)            #fügt den aktuellen Titel als Knoten in den Bau        

        # print("Titel",self.label,depth)

        #hier connections mit vorherigem
        # if(not depth == 0):
        #     g.add_edge(self.label,last_label)   #fügt Kante zum Vorgänger hinzu
        #     print(f"fügt Kante von {self.label} nach {last_label} hinzu")
        # if(self.first):
        #     last_label = self.label
        #     self.first = False
        
        
        #muss keine titel finden, da das im nächsten schritt gemacht wird

        #noch die Abfrage, ob noch mal Rekursion
        if(depth<3):

            #holt die nächsten Links aus der aktuellen HTML Seite
            tmp_links_list = re.findall("a\shref=\"\/wiki\/.*?\"",self.HTML)
            links_list2 = []
            for entry in tmp_links_list:    
                if (not re.search(r":",entry)): #entfernt Links, die nicht auf "richtige" wiki Seiten verweisen
                    tmp = re.sub("a\shref=\"","",entry)
                    links_list2.append(tmp)
            links_list = []
            for entry in links_list2:
                tmp = re.sub("\"","",entry)
                links_list.append(tmp) #links_list ist die Liste mit den neuen Links

            depth = depth+1
            self.first = True
            
            g.add_vertex(self.label)
            node = g.get_vertex(self.label)

            #rekursions Schritt
            i = 0
            for link in links_list:
                if i<5:
                    new_label = self.find_titel("https://en.wikipedia.org"+link)
                    node.add_adjacent(new_label)

                    #print("label",self.label,depth)
                    #print("---------------------------node------------------",node.get_label())
                    e = node.get_label()
                    #print(f"Kante: {new_label} -> {e}")
                    self.find_all_links("https://en.wikipedia.org"+link,last_label,depth)    
                    i = i+1
                
            


if __name__ == "__main__":

    g = graphClass.Graph()

    # g.add_vertex("test1")
    # g.add_vertex("test2")
    # g.add_vertex("test3")

    # g.add_edge("test2","test3")
    # g.add_edge("test1","test2")


    
    #https://en.wikipedia.org noch davor
    #https://en.wikipedia.org/wiki/Valuative_criterion
    #url = "https://en.wikipedia.org/wiki/Valuative_criterion"
    url ="https://en.wikipedia.org/wiki/Newick_format"
    #url = "https://en.wikipedia.org/wiki/Sursurunga_language"
    #url = "https://en.wikipedia.org/wiki/Germany"
    #url = "https://en.wikipedia.org/wiki/Chris_Alp"
    K=500
    D=10
    i=0
    j=0
    #while(i<=K and j<=D):
    q = Query(g)
    q.find_all_links(url,None,0)

    print()
    for v in g:
        print(v.get_label())
        for n in v.get_adjacent():
            a = v.get_label()
            b = n
            print(f"parent: {a}, nachbar: {b}")

    
    for e in g:
        print(e.get_label())


#bugs :
# am ender einer Rekursion findet er keinen Titel
#