import slicing
import graph
import os
import match
import networkx as nx
from pylab import show
import matplotlib.pyplot as plt
import productVideo

lenOfPic = 0   # height of picture/video
widOfPic = 0   # length of picture/video

"""
* objective: write video
* input: path - working directory; 
         listOfPic - the list of all of pictures, the entire content of the video; 
         listOfRec - the list of all of rectangles in the video
         numOfPic - the number of pictures
* output: nothing
"""
def writeVideo(path, listOfPic, listOfRec, numOfPic):

    global lenOfPic
    global widOfPic

    lenOfPic = len(listOfPic[0][0])
    widOfPic = len(listOfPic[0])
    graphPoints = []

    for i in range(0, numOfPic):         # the i th picture in the video

        # get list of all of information of rectangles in the i th picture
        temp = slicing.slicingFunction(listOfPic[i], listOfRec[i], i+1, path, widOfPic, lenOfPic)
        graphPoints.append(temp)

    graphs = []
    x = 0

    # to found a directory
    if not os.path.exists(path + '/GXL'):
        os.makedirs(path + '/GXL')

    for graphPoint in graphPoints:
        # to create graphs for pictures according to the list of all of information of rectangles
        # threshold = 150
        G = graph.createGraph(graphPoint, 150)

        # to save these graphs
        graph.writeGraph(G, x, path+"/GXL/")
        graphs.append(G)
        x += 1

    for i in range(0, len(graphs)-1):
        match.match2Graph(graphs[i], graphs[i+1])
        drawNewGraph(graphs[i], path, i)
    drawNewGraph(graphs[len(graphs)-1], path, len(graphs)-1)

    size = (lenOfPic, widOfPic)

    productVideo.picvideo(path+'/graphs', size)

    print("done")


"""
* objective: draw graphs after matching
* input: aGraph - a graph matched
* output: nothing, but generate graphs
"""
def drawNewGraph(aGraph, path, x):
    colorSequence = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
    positionOfPoint = {}
    colorOfPoint = ()
    listOfPoint = []
    labOfPoint = {}
    for i in range(0, len(aGraph.nodes)):
        positionOfPoint[i] = (aGraph.nodes[i]['x'], aGraph.nodes[i]['y'])
        colorOfPoint += (colorSequence[aGraph.nodes[i]['order'] % len(colorSequence)],)
        listOfPoint.append(aGraph.nodes[i]['order'])
        labOfPoint[i] = aGraph.nodes[i]['order']

    fig = plt.figure(1, figsize=(lenOfPic / 100, widOfPic / 100))
    nsize = 100

    # Draw graph
    nx.draw(aGraph,
            pos=positionOfPoint,
            labels=labOfPoint,
            node_color=colorOfPoint,
            node_shape='.',
            node_size=nsize)

    try:
        if not os.path.exists(path + '/graphs'):
            os.makedirs(path + '/graphs')
    except OSError:
        print('Error: Creating directory of graphs !')

    plt.savefig(path+'/graphs/'+str(x)+'.jpg')
    show()
    print("done drawNewGraph")
