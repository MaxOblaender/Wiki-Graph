import sys
import argparse
from wikigraph.graphClass import Graph
from wikigraph.queryClass import Query
from wikigraph.drawClass import Draw

def main():
    """Cli mittels argparse"""
    parser = argparse.ArgumentParser(prog="graph",description="displays wikipeadia pages")

    parser.add_argument( #für den link
        "link",
        # default="https://en.wikipedia.org/wiki/Tacoma_Narrows_Bridge",
        type=str, 
        help="enter a wikipedia link to search in. Worky only on english wikipedia sites"
    )
    parser.add_argument(
        "-k",
        default=500,
        type=int,
        help="max. amount of nodes in the graph"
    )
    parser.add_argument(
        "-d",
        default=10,
        type=int,
        help="max. amount of steps from the original site"
    )
    parser.add_argument(
        "-s",
        "--show",
        default="",
        type=str,
        help="string to get highlighted in finished graph"
    )
    parser.add_argument( #sonst stdout. Gibt den Graphen im nx "spring" layout aus.
        "-p",
        "--picture",
        default=False,
        action="store_true",
        help="draws the graph using networkx (spring_layout)"
    )
    parser.add_argument( # Gibt den Graphen im nx "spiral" layout aus.
        "-ps",
        "--picturespiral",
        default=False,
        action="store_true",
        help="draws the graph using networkx (spiral_layout)"
    )
    parser.add_argument( # Gibt den Graphen im nx "planar" layout aus.
        "-pp",
        "--pictureplanar",
        default=False,
        action="store_true",
        help="draws the graph using networkx (planar_layout)"
    )
    args = parser.parse_args()   

    q = Query(args.link,args.k,args.d) #startet auch schon direkt die Suche

    if args.picture:
        q.draw(q.g,"spring",args.show)
    elif args.picturespiral:
        q.draw(q.g,"spiral",args.show)
    elif args.pictureplanar:
        q.draw(q.g,"planar",args.show)
    else:
        print(q.g)

if __name__ == '__main__':
    main()