#!/usr/bin/python

# Reads a text file and creates a graph as a list of edges, each edge has a random weight.

from Graph import *
import random

def ReadGraphFile (fn) :
    f = open (fn)
    max_node = 0
    lines = f.readlines()
    # G = Graph ()
    # for line in lines :
    #     if line[0] == "#" :
    #         continue

    #     node1, node2 = map(int, line[:-1].split())
    #     print node1, node2
    #     G.add_edge (node1, node2)

    # print G.edges

    edges_list = []
    weigth_list = []
    for line in lines :
        if line[0] == "#" :
            continue

        edges_list.append(map(int, line[:-1].split()))
        weight_list.append (random.random(0,1))

def CreateRandomGraphs (num_graphs, edges, probs) :
    graph_snapshots = []
    for i in range (num_graphs) :
        tmp_graph = Graph ()
        for edge, prob in zip(edges, probs) : 
            rand = random.random(0,1)
            if rand < prob :
                tmp_graph.add_edge (edge[0], edge[1])
        graph_snapshots.append(tmp_graph)

    return graph_snapshots

ReadGraphFile ("data/ca-HepTh.txt")
