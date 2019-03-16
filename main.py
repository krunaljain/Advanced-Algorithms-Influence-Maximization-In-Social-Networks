#!/usr/local/bin/python3.6

import sys, random
from Graph import *
from ReadDataset import *
from Heuristic import *
from InfluenceUtility import *
sys.setrecursionlimit(100000)
import matplotlib.pyplot as pyplot;
import time;



# random.seed(0)

def main () :
    edges_list, weight_list, nodes_set = ReadGraphFile (sys.argv[1])
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

    step_size = 1;
    threshold = 10;
    totalNodes = range(0, 101);

    optimizedGreedyHeuristic = [];
    greedyHeuristic = [];
    randomHeuristic = [];
    optimizedGreedyHeuristic.append(0);
    greedyHeuristic.append(0);
    randomHeuristic.append(0);

    # print (len(influence.find_influence(set([65687]), graph_snaps, threshold)))
    # print (len(influence.find_influence(set([44262]), graph_snaps, threshold)))
    influenceMap = getInfluenceMap(nodes_set,graph_snaps,threshold);
    optimizedGreedyHeuristicSelectedSet = set();
    greedyHeuristicSelectedSet = set();
    randomHeuristicTime = [];
    randomHeuristicTime.append(0);
    optimizedGreedyHeuristicTime = [];

    optimizedGreedyHeuristicTime.append(0);
    greedyHeuristicTime = [];
    greedyHeuristicTime.append(0);

    for k in totalNodes :
        print ("k = ", k)

        if k == 0:
            continue;

        startTime = time.time();
        randomHeuristicCount = random_heuristic(graph_snaps, nodes_set, k, step_size, threshold);
        randomHeuristicTime.append(time.time() - startTime);
        randomHeuristic.append(randomHeuristicCount);

        startTime = time.time();
        influenceSet = heuristic1(graph_snaps, nodes_set, k, step_size, threshold,influenceMap,optimizedGreedyHeuristicSelectedSet);
        optimizedGreedyHeuristicTime.append(time.time() - startTime);
        # print(influenceSet);
        print("Size of influenced set is ", len(influenceSet));


        # print ("random influenced set is ", influenceSetRandom)
        optimizedGreedyHeuristicCount = len(influenceSet);
        startTime = time.time();
        greedyHeuristicCount = len(heuristic2(graph_snaps,nodes_set,k,step_size,threshold,influenceMap,greedyHeuristicSelectedSet));
        greedyHeuristicTime.append(time.time() - startTime);
        print("Size of influenced set by greedy heuristic is ", greedyHeuristicCount);


        print ("Size of influenced set by random heuristic is ", randomHeuristicCount)

        optimizedGreedyHeuristic.append(optimizedGreedyHeuristicCount);
        greedyHeuristic.append(greedyHeuristicCount);
        print("Selected set for optimized greedy heuristic is ", optimizedGreedyHeuristicSelectedSet);
        print("Selected set for  greedy heuristic is ", greedyHeuristicSelectedSet);


    pyplot.plot(totalNodes, optimizedGreedyHeuristic, '-b', label='Optimized Greedy Heuristic')
    pyplot.plot(totalNodes, greedyHeuristic, '-r', label='Greedy Heuristic')
    pyplot.plot(totalNodes, randomHeuristic, '-g', label='Random Heuristic')

    pyplot.legend(loc='upper left')
    pyplot.ylabel('Total nodes influnced');
    pyplot.xlabel('Total nodes selected');
    pyplot.show()

    pyplot.plot(totalNodes, optimizedGreedyHeuristicTime, '-b', label='Optimized Greedy Heuristic')
    pyplot.plot(totalNodes, greedyHeuristicTime, '-r', label='Greedy Heuristic')
    pyplot.plot(totalNodes, randomHeuristicTime, '-g', label='Random Heuristic')

    pyplot.legend(loc='upper left')
    pyplot.ylabel('Total execution time');
    pyplot.xlabel('Total nodes selected');
    pyplot.show()
    pyplot.savefig('greedy_heuristics_time');


main ()
