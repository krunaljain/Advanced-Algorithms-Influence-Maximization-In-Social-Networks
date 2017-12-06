#!/usr/local/bin/python3.6

def find_influence (source_nodes, graph_snapshots, threshold) :
    influenced_node_count = {} # this contains nodes and count for each node
    for G in graph_snapshots :
        S = G.find_reachable_nodes (source_nodes)
        # Update influenced_node_count looking at S
        for node in S :
            if node in influenced_node_count :
                influenced_node_count[node]+=1
            else :
                influenced_node_count[node] = 1

    influenced_nodes = set([])
    for node in influenced_node_count :
        if influenced_node_count [node] > threshold:
            influenced_nodes.add (node)

    # We do not want source nodes in the influenced set. Remove any nodes that are there in source nodes from influenced_nodes.
    for node in source_nodes :
        if node in influenced_nodes :
            influenced_nodes.remove (node)

    return influenced_nodes
