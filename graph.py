import networkx as nx
from pylab import show
import matplotlib.pyplot as plt
import writeVideo
import xml.dom.minidom

"""
* objective: write graph in a .gxl file
* enter: graph - a graph; x - order of graph; path - working directory
* return: nothing
"""
def writeGraph(graph, x, path):

    # create a new empty file in memory
    doc = xml.dom.minidom.Document()

    # create a root
    root = doc.createElement("root")
    doc.appendChild(root)

    # add all nodes and their information
    for i in range(0, graph.number_of_nodes()):
        node = doc.createElement("node_"+str(i))
        root.appendChild(node)
        node.setAttribute('x', str(graph.nodes[i]['x']))
        node.setAttribute('y', str(graph.nodes[i]['y']))
        node.setAttribute('lenghtOfRec', str(graph.nodes[i]['lenghtOfRec']))
        node.setAttribute('heightOfRec', str(graph.nodes[i]['heightOfRec']))
        node.setAttribute('r', str(int(graph.nodes[i]['r'])))
        node.setAttribute('g', str(int(graph.nodes[i]['g'])))
        node.setAttribute('b', str(int(graph.nodes[i]['b'])))
        node.setAttribute('order', str(graph.nodes[i]['order']))

        # add edges
        neighbor = []
        for j in list(graph.edges(i)):
            neighbor.append(j[1])
        node.setAttribute('neighbor', str(neighbor))
        continue

    # open a new empty file in disk
    fp = open(path+str(x)+".gxl",'w')

    # write the graph in this empty file
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


"""
* objective: create the graph
* enter: listOfGraph - all of rectangles information in a picture, threshold - correlation
* return: G - a graph
"""
def createGraph(listOfGraph, threshold):
    # create a void graph
    G = nx.Graph()

    # position of all of points
    positionOfPoint = {}

    # color of points
    colorOfPoint = ()

    # for every point:
    for i in range(0, len(listOfGraph)):

        # add a node in this graph, and we add all of information of this node as attribute
        G.add_node(i,
                   x=listOfGraph[i][0][1],
                   y=listOfGraph[i][0][0],
                   widthOfRec=listOfGraph[i][1][0],
                   heigthOfRec=listOfGraph[i][1][1],
                   r=listOfGraph[i][2][0],
                   g=listOfGraph[i][2][1],
                   b=listOfGraph[i][2][2],
                   order=i)

        # the i th node position
        # x=listOfGraph[i][0][1]
        # y=listOfGraph[i][0][0]
        positionOfPoint[i] = (listOfGraph[i][0][1], listOfGraph[i][0][0])

        # turn RGB to Hex and add it in colorOfPoint array
        colorOfThisPoint = "#"
        for j in range(0, 3):
            a = str(hex(int(listOfGraph[i][2][j])))[2:]
            if len(a) == 1:
                a = '0' + a
            colorOfThisPoint += a
        colorOfPoint += (colorOfThisPoint,)

    # draw edges
    for i in range(0, len(listOfGraph) - 1):
        for j in range(i + 1, len(listOfGraph)):

            # calculate distance between node i and node j, the Pythagorean theorem
            d = pow(
                pow(listOfGraph[i][0][0] - listOfGraph[j][0][0], 2) + pow(listOfGraph[i][0][1] - listOfGraph[j][0][1],
                                                                          2), 0.5)
            if d < threshold:
                G.add_edge(i, j)

    # Canvas size = video size
    # this method is to keep the same size of all pictures
    fig = plt.figure(1, figsize=(writeVideo.lenOfPic / 100, writeVideo.widOfPic / 100))

    # node size
    nsize = 100

    # draw this graph
    nx.draw(G,
            pos=positionOfPoint,
            with_labels=True,
            node_color=colorOfPoint,
            node_shape='.',
            node_size=nsize)

    # save this graph whose name is ba.png
    # plt.savefig("ba.png")
    show()
    return G