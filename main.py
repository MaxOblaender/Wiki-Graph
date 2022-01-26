import graphClass
import queryClass

if __name__ == "__main__":

    g = graphClass.Graph()

    g.add_vertex("test1")
    g.add_vertex("test2")
    g.add_vertex("test3")

    g.add_edge("test2","test3")
    g.add_edge("test1","test2")


    for v in g:
        print("lable:"+v.lable)
        for c in v.get_children():
            print("parent:",v.get_lable(),"child:",c.get_lable())

    #https://en.wikipedia.org noch davor
    url ="https://en.wikipedia.org/wiki/Newick_format"
    K=500
    D=10
    i=0
    j=0
    #while(i<=K and j<=D):
    queryClass.Query(url,g)
    
