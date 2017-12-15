#!/usr/local/bin/python3.6

import sys, random
from Graph import *
from ReadDataset import *
from Heuristic import *
from InfluenceUtility import *
sys.setrecursionlimit(100000)

# random.seed(0)

def main () :
    edges_list, weight_list, nodes_set = ReadGraphFile ("data/ca-HepTh.txt")
    graph_snaps = CreateRandomGraphs (50, edges_list, weight_list)

    # for graph in graph_snaps :
    #     print ("new graph")
    #     graph.print_graph ()
    # y = []
    # for i in range (1,10) :
    #     l = len((find_influence (set([24325]), graph_snaps, i)))
    #     print (l)
    #     y.append(l)
    
    # np.plot (range (1,10), y)
    # np.show ()
    
    # i = 0
    # nodes_list = list(nodes_set)
    # for i in range(len(nodes_list)-10) :
    #     # print (i, len(find_influence (set([nodes_list[i], nodes_list[i+1], nodes_list[i+2], nodes_list[i+3], nodes_list[i+4]]), graph_snaps, 45)))
    #     print (i, nodes_list[i], len(find_influence (set([nodes_list[i]]), graph_snaps, 30)))

    empty_set = set([])
    step_size = 1;
    threshold = 10;

    # print (len(influence.find_influence(set([65687]), graph_snaps, threshold)))
    # print (len(influence.find_influence(set([44262]), graph_snaps, threshold)))
    influenceMap = getInfluenceMap(nodes_set,graph_snaps,threshold);
    for k in range (20,21) :
        print ("k = ", k)
        influenceSet = heuristic1(graph_snaps, nodes_set, k, step_size, threshold,influenceMap);
        # print(influenceSet);
        print("Size of influenced set is ", len(influenceSet));

        print("Size of influenced set by greedy heuristic is ", len(heuristic2(graph_snaps,nodes_set,k,step_size,threshold,influenceMap)))

        # print ("random influenced set is ", influenceSetRandom)
        print ("Size of influenced set by random heuristic is ", random_heuristic (graph_snaps, nodes_set, k, step_size, threshold))

main ()
