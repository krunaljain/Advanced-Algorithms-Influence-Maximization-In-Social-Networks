#!/usr/local/bin/python3.6
import  InfluenceUtility as influence

def heuristic1 (graph_snaps, nodes_set, k, step_size) :
    pass
    # graph_snaps: graph snapshots
    # nodes_set: set of nodes in the complete graph
    # k: number of nodes to influence initially
    # step_size: number of nodes to add to the opt set every iteration


    maxLength = 0;
    bestNode = 0;
    bestNodeSet = set();
    uninfluencedNodes = nodes_set;
    for i in range(k):
        influencedMap = {};
        maxLength = 0;
        maxNode = 0;

        for uninfluenced_node in uninfluencedNodes:
            current_node = set();
            current_node.add(uninfluenced_node);
            threshold = 30;
            influencedMap[uninfluenced_node] = set.intersection(uninfluencedNodes, influence.find_influence(current_node,graph_snaps,threshold));
            new_nodes_influenced = len(influencedMap[uninfluenced_node]);
            if maxLength < new_nodes_influenced:
                maxLength = new_nodes_influenced;
                maxNode = uninfluenced_node;

        bestNodeSet.add(maxNode);
        uninfluencedNodes.discard(maxNode);
        uninfluencedNodes.discard(influencedMap[maxNode]);

    print(bestNodeSet)
    return  bestNodeSet;


    # find the influence of each vertex
    # create a dict vert_influence with key as node and value as the set of nodes influenced by node 
    # best_node = node with the largest influence
    # best_set = set(best_node)
    # uninfluenced_set = nodes_set

    # repeat k times
    #   uninfluenced_set = uninfluenced_set - influence set of best node
    #   for every node in uninfluenced set
    #     num_new_influences = len(influence set of node from the dict created earlier    intersection     uninfluenced set)
    #   find best_node - the node which produces maximum num_new_influences
    #   add best_node to best_set
    # return best_set
