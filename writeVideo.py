import slicing
import graph
import os
import match
import networkx as nx
from pylab import show
import matplotlib.pyplot as plt
import productVideo
import cv2

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

    productVideo.picvideo(path + '/graphs', size)
    productVideo.picvideo(path + '/imgTest', size)

    print("done")


"""
* objective: draw graphs and pictures after matching
* input: aGraph - a graph matched
*        path - work path
*        x - index of picture / graph
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

    # turn a letter to an array, because cv2.rectangle can only use 3 numbers of RGB
    colorOfRec = getColorOfRec(colorOfPoint)

    # save graphs in drive
    try:
        if not os.path.exists(path + '/graphs'):
            os.makedirs(path + '/graphs')
    except OSError:
        print('Error: Creating directory of graphs !')

    plt.savefig(path+'/graphs/'+str(x)+'.jpg')
    show()
    print("done drawNewGraph")

    # save pictures with colorful rectangles in folder named 'imgTest'
    try:
        if not os.path.exists(path + '/imgTest'):
            os.makedirs(path + '/imgTest')
    except OSError:
        print('Error: Creating directory of graphs !')

    # those pictures made by video are saved in folder 'img1'
    filelist = os.listdir(path + '/img1/')
    items = sorted(filelist)
    indexOfPic = 0
    for y in range(0, len(items)):
        if items[y].endswith('.jpg'):
            if indexOfPic == x:
                image = cv2.imread(path + '/img1/' + items[y])

                # draw those rectangles in a picture
                for indexOfNode in range(0, len(aGraph.nodes)):
                    xmin = int(aGraph.nodes[indexOfNode]['x'] - aGraph.nodes[indexOfNode]['widthOfRec'] / 2)
                    ymin = int(aGraph.nodes[indexOfNode]['y'] - aGraph.nodes[indexOfNode]['heightOfRec'])
                    xmax = int(aGraph.nodes[indexOfNode]['x'])
                    ymax = int(aGraph.nodes[indexOfNode]['y'] + aGraph.nodes[indexOfNode]['heightOfRec'])
                    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), colorOfRec[indexOfNode], 2)

                cv2.imwrite(path + '/imgTest/' + str(indexOfPic) + '.jpg', image)
                print("done drawNewPic")
                return
            else:
                indexOfPic += 1

"""
* Objective: turn those color to RGB
* input: colorOfPoint - an array of colors, we use it in networkX.draw
* output: colorOfRec - a dictionary of arrays, every array is a RGB color of a rectangle
"""
def getColorOfRec(colorOfPoint):
    colorOfRec = []
    for color in colorOfPoint:
        if color == 'b':
            colorOfRec.append((255, 0, 0))
        elif color == 'g':
            colorOfRec.append((0, 255, 0))
        elif color == 'r':
            colorOfRec.append((0, 0, 255))
        elif color == 'c':
            colorOfRec.append((255, 255, 0))
        elif color == 'm':
            colorOfRec.append((255, 0, 255))
        elif color == 'y':
            colorOfRec.append((0, 255, 255))
        elif color == 'k':
            colorOfRec.append((255, 255, 255))
        else:
            colorOfRec.append((0, 0, 0))
    return colorOfRec