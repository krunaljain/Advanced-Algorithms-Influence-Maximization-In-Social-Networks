#!/usr/local/bin/python3.6

class Graph :
    def __init__ (self) :
        self.edges = {}

    def add_edge (self, from_, to) :
        if from_ not in self.edges :
            self.edges[from_] = [to]
        else :
            self.edges[from_].append(to)

        if to not in self.edges :
            self.edges[to] = []

    def find_reachable_nodes (self, source_nodes) :
        # source nodes is a list of nodes
        reached = set([])
        for node in source_nodes :
            if node in self.edges :
                self.dfs (node, reached)

        return reached

    def dfs (self, node, reached) :
        for nbr in self.edges[node] :
            if nbr not in reached :
                reached.add (nbr)
                self.dfs (nbr, reached)

    def print_graph (self) :
        for node in self.edges :
            print (node, ": ", self.edges[node])

def test () :
    G = Graph ()
    G.add_edge (0,1)
    G.add_edge (1,2)
    G.add_edge (2,3)
    G.add_edge (1,4)
    print (G.find_reachable_nodes ([1]))

if __name__ == "__main__" :
    test ()
