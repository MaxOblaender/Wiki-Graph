import graphClass
import requests
import re

class Query():
    """Klasse zum holen und verarbeiten der HTML-Seiten"""
    g = graphClass.Graph
    def __init__(self,url,graph):
        self.HTML = requests.get(url).text    
        self.g = graph
        self.find_all_links()

    def find_all_links(self):
        #findet alle "a href" und setzt eigenen titel
        tmp_title_list = re.findall("<title>.*-",self.HTML)
        tmp_title = tmp_title_list[0]
        tmp_title = re.sub("<title>","",tmp_title)
        self.lable = re.sub("\s-","",tmp_title)

        print(self.lable)

        #muss keine titel finden, da das im nächsten schritt gemacht wird
        tmp_links_list = re.findall("a\shref=\"\/wiki\/.*?\"",self.HTML)
        print("liste0")
        print(tmp_links_list)
        links_list2 = []
        for entry in tmp_links_list:
            tmp = re.sub("a\shref=\"","",entry)
            links_list2.append(tmp)
        print("list2",links_list2)
        links_list = []
        for entry in links_list2:
            tmp = re.sub("\"","",entry)
            links_list.append(tmp)
        print("list1")
        print(links_list)


