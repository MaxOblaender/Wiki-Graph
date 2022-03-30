from .graphClass import Graph
from .drawClass import Draw
import requests
import re

class Query():
    """Klasse zum holen und verarbeiten der HTML-Seiten"""
    g = Graph()

    def __init__(self,url,max_amount,max_depth):
        """setzt den Graphen"""
        self.g = Graph()
        self.queue = [] # die liste wird als quasi queue verwendet um die Tiefe richtig zu zählen
        self.max_amount = max_amount #max anzahl an Seiten
        self.max_depth = max_depth  #max anzahl an Tiefe
        self.run(url,0,0)

    def find_titel(self,url):
        """Setzt den titel(label) aus der HTML Seite"""
        try:
            HTML = requests.get(url).text
        except:
            HTML = requests.get("https://en.wikipedia.org/wiki/"+url).text
        tmp_title_list = re.findall("<title>.*-",HTML)
        try:    #falls kein Titel gefunden werden kann
            tmp_title = tmp_title_list[0] 
        except:
            print("no title in",url)
            return "no title found"
        tmp_title = re.sub("<title>","",tmp_title)
        return re.sub("\s-","",tmp_title) 

    def find_all_links(self,label):
        """findet alle weiterführenden Links"""
        HTML = requests.get("https://en.wikipedia.org/wiki/"+label).text #holt html von Seite
        #holt die nächsten Links aus der aktuellen HTML Seite
        all_links = re.findall("a\shref=\"\/wiki\/.*?\"",HTML) 
        proper_links = []
        for entry in all_links:    
            if (not re.search(r":",entry) and not re.search("Main\_Page",entry)): #entfernt Links, die nicht auf "richtige" wiki Seiten verweisen
                tmp = re.sub("a\shref=\"\/wiki\/","",entry)
                tmp = re.sub("\"","",tmp)
                proper_links.append(tmp)
        return proper_links  

    def run(self,url,depth,amount):
        """Hauptmethode für die Iteration"""
        labelroot = self.find_titel(url) #findet titel der ersten Seite
        self.g.add_vertex(labelroot) #fügt Wurzel in Graphen g
        self.queue.append(labelroot) #fügt Wurzel in die queue
        amount = amount +1 #K
        self.queue.append("$") #fügt (besonderes) Element in die queue, welches aufzeigt, wenn nächste Tiefe erreicht wird

        while depth < self.max_depth and amount < self.max_amount:
            print("amount: ",amount)
            if self.queue[0] == "$": #nur an erster Stelle in queue, wenn neuer Abstand von Wurzel erreicht wird
                depth = depth + 1
                self.queue.append("$") #enqueue
                self.queue.pop(0) #dequeue
                print("new depth")

            all_links = self.find_all_links(self.queue[0])

            for link in all_links:
                if amount < self.max_amount:
                    self.queue.append(link) #fügt gefundenen Link in die queue ein
                    titel = self.find_titel("https://en.wikipedia.org/wiki/"+link) 
                    self.g.add_vertex(titel)
                    self.g.add_edge(self.find_titel(self.queue[0]),titel) #fügt Kante von dem ersten element der Queue (Elter der aktuellen Seite) zur aktuellen Seite hinzu
                    amount = amount + 1
            
            self.queue.pop(0) #Link an erster Stelle der queue wurde abgearbeitet
            print("----------------------pop-----------------")

        print("finished with: ",amount," ",depth)
        # self.draw(self.g)

    def draw(self,graph,form,show):
        """Methode für die darstellung des Graphen. Benutzt die Klasse Draw"""
        draw_class = Draw(graph,form,show)
        

        # g.add_vertex(self.label)            #fügt den aktuellen Titel als Knoten in den Bau        

        # print("Titel",self.label,depth)

        #hier connections mit vorherigem
        # if(not depth == 0):
        #     g.add_edge(self.label,last_label)   #fügt Kante zum Vorgänger hinzu
        #     print(f"fügt Kante von {self.label} nach {last_label} hinzu")
        # if(self.first):
        #     last_label = self.label
        #     self.first = False
        
        
        # #muss keine titel finden, da das im nächsten schritt gemacht wird

        # #noch die Abfrage, ob noch mal Rekursion
        # if(depth < self.max_depth and amount < self.max_amount): #hier nur depth

        #     #holt die nächsten Links aus der aktuellen HTML Seite
        #     tmp_links_list = re.findall("a\shref=\"\/wiki\/.*?\"",self.HTML)
        #     links_list2 = []
        #     for entry in tmp_links_list:    
        #         if (not re.search(r":",entry)): #entfernt Links, die nicht auf "richtige" wiki Seiten verweisen
        #             tmp = re.sub("a\shref=\"","",entry)
        #             links_list2.append(tmp)
        #     links_list = []     #kann man das nicht in eine Schleife packen?
        #     for entry in links_list2:
        #         tmp = re.sub("\"","",entry)
        #         links_list.append(tmp) #links_list ist die Liste mit den neuen Links

        #     depth = depth+1 #stimmt nicht unbedingt, da ja nur depth für hier diesen zweig
        #     print("depth: ",depth)
            
        #     g.add_vertex(self.label) #fügt aktuelle seite als Knoten in den Graphen g
        #     print(self.label)
        #     node = g.get_vertex(self.label) #ist das aktuelle Vertex element

        #     #rekursions Schritt
        #     #amount = amount + len(links_list) #das muss noch richtig überarbeitet werden. Vielleicht in der for schleife jedes mal hoch zählen und keinen aufruf mehr machen
        #     # print("amount",amount)
        #     next_links = []
        #     for link in links_list:
        #         if amount < self.max_amount: #hier noch mal amount < 500 abfragen
        #             new_label = self.find_titel("https://en.wikipedia.org"+link) #durchsucht das englische Wikipedia
        #             node.add_adjacent(new_label)
        #             amount = amount+1 #vor oder nach dem nächsten rekursionsaufruf? glaube hier schon richtig
        #             next_links.append(link)
        #                     #print("label",self.label,depth)
        #                     #print("---------------------------node------------------",node.get_label())
        #             # e = node.get_label() #was hier???????????????????
        #                     #print(f"Kante: {new_label} -> {e}")
        #             # self.find_all_links("https://en.wikipedia.org"+link,last_label,depth,amount) #last_label noch relevant?  ne
                    
        #             print("amount:",amount)  
        #     for link in next_links:
        #         self.run("https://en.wikipedia.org"+link,last_label,depth,amount)

        
                   
                    
            


# if __name__ == "__main__":

#     g = graphClass.Graph()

    # g.add_vertex("test1")
    # g.add_vertex("test2")
    # g.add_vertex("test3")

    # g.add_edge("test2","test3")
    # g.add_edge("test1","test2")


    
    #https://en.wikipedia.org noch davor
    #https://en.wikipedia.org/wiki/Valuative_criterion
    # url = "https://en.wikipedia.org/wiki/Valuative_criterion"
    # url ="https://en.wikipedia.org/wiki/Newick_format"
    # url = "https://en.wikipedia.org/wiki/Germany"
    # url = "https://en.wikipedia.org/wiki/Pierre-Jules_Cavelier"
    # url = "https://en.wikipedia.org/wiki/Chris_Alp"
    # url = "https://en.wikipedia.org/wiki/Tacoma_Narrows_Bridge"

    # q = Query(url,g,500,8)
    
    # print(g)

    # print()
    # for v in g:
    #     print(v.get_label())
    #     for n in v.get_adjacent():
    #         a = v.get_label()
    #         b = n
    #         print(f"parent: {a}, nachbar: {b}")

    
    #print(g)


#todo:
# 1. ausgabe des Graphen als txt form
# 2. commandline tool -> -h usw
# 3. Zusatzaufgabe: Eingabe string Node rot unterlegen
# 3. Bildausgabe schöner machen