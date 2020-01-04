import networkx as nx

a = 1

"""
* objective: match 2 graphs
* input: G1 - the first graph
         G2 - the second graph
* output: nothing, but change G2, matching information is saved in G2.nodes[i]['order']
"""
def match2Graph(G1,G2):
    global a

    # obtain min_edit_path and min_edit_distance
    para2, para3 = nx.optimal_edit_paths(G1, G2)
    maxOrder = 0
    for i in range(0, len(G1.nodes)):
        if G1.nodes[i]['order'] > maxOrder:
            maxOrder = G1.nodes[i]['order']

    # match 2 graph
    for i in range(0,len(para2[0][0])):
        if (para2[0][0][i][0] != None) and (para2[0][0][i][1] != None):
            G2.nodes[para2[0][0][i][1]]['order'] = G1.nodes[para2[0][0][i][0]]['order']
        elif para2[0][0][i][0] == None:
            maxOrder += 1
            G2.nodes[para2[0][0][i][1]]['order'] = maxOrder
        else:
            continue

    for paraTemp in para2:
        matchNumber = 0
        for matchNodes in paraTemp[0]:
            if matchNodes[0] != matchNodes[1]:
                matchNumber += 1

    print(para3)