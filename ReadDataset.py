#!/usr/local/bin/python3.6

# Reads a text file and creates a graph as a list of edges, each edge has a random weight.

from Graph import *
import sys, random
# from InfluenceUtility import *
# sys.setrecursionlimit(100000)
# import matplotlib.pyplot as np

def ReadGraphFile (fn) :
    f = open (fn)
    lines = f.readlines()

    edges_list = []
    weight_list = []
    nodes_set = set([])
    for line in lines :
        if line[0] == "#" :
            continue

        node1, node2 = map(int, line[:-1].split())
        edges_list.append ([node1, node2])

        # TODO: assign num parallel edges here and use it to assign a probability for each edge.
        weight_list.append (random.random()/3)
        # weight_list.append (1)
        nodes_set.add(node1)
        nodes_set.add(node2)

    return edges_list, weight_list, nodes_set

def CreateRandomGraphs (num_graphs, edges, probs) :
    graph_snapshots = []
    for i in range (num_graphs) :
        tmp_graph = Graph ()
        for edge, prob in zip(edges, probs) : 
            rand = random.random()
            if rand < prob :
                tmp_graph.add_edge (edge[0], edge[1])
        graph_snapshots.append(tmp_graph)

    return graph_snapshots

