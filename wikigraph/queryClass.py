from .graphClass import Graph
from .drawClass import Draw
import requests
import re

class Query():
    """Klasse zum Abfragen und Verarbeiten der HTML-Seiten"""
    g = Graph()

    def __init__(self,url,max_amount,max_depth):
        """setzt den Graphen und startet die Suche"""
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
        HTML = requests.get("https://en.wikipedia.org/wiki/"+label).text #holt html von Seite. Durchsucht immer englische Wiki Seiten
        #holt die nächsten Links aus der aktuellen HTML Seite
        all_links = re.findall("a\shref=\"\/wiki\/.*?\"",HTML) 
        proper_links = []
        for entry in all_links:    
            if (not re.search(r":",entry) and not re.search("Main\_Page",entry)): #entfernt Links, die nicht auf "richtige" Wiki Seiten verweisen
                tmp = re.sub("a\shref=\"\/wiki\/","",entry)
                tmp = re.sub("\"","",tmp)
                proper_links.append(tmp)
        return proper_links  #Am Ende sind die "Links" nur noch die Label

    def run(self,url,depth,amount):
        """Hauptmethode für die Iteration"""
        labelroot = self.find_titel(url) #findet titel der ersten Seite
        self.g.add_vertex(labelroot) #fügt Wurzel in Graphen g
        self.queue.append(labelroot) #fügt Wurzel in die queue
        amount = amount +1 #K
        self.queue.append("$") #fügt (besonderes) Element in die queue, welches aufzeigt, wenn nächste Tiefe erreicht wird

        while depth < self.max_depth and amount < self.max_amount:
            if self.queue[0] == "$": #nur an erster Stelle in queue, wenn neuer Abstand von Wurzel (D) erreicht wird
                depth = depth + 1
                self.queue.append("$") #enqueue
                self.queue.pop(0) #dequeue

            all_links = self.find_all_links(self.queue[0]) #findet die Links auf der Ursprungs Seite

            for link in all_links:
                if amount < self.max_amount: 
                    self.queue.append(link) #fügt gefundenen Link in die queue ein
                    titel = self.find_titel("https://en.wikipedia.org/wiki/"+link) 
                    self.g.add_vertex(titel)
                    self.g.add_edge(self.find_titel(self.queue[0]),titel) #fügt Kante von dem ersten element der Queue (Elter der aktuellen Seite) zur aktuellen Seite hinzu
                    amount = amount + 1
            
            self.queue.pop(0) #Link an erster Stelle der queue wurde abgearbeitet

        print("finished with K= ",amount," and D=",depth)

    def draw(self,graph,form,show):
        """Methode für die darstellung des Graphen. Benutzt die Klasse Draw"""
        draw_class = Draw(graph,form,show)        