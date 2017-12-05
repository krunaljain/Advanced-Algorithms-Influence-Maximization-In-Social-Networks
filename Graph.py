#!/usr/bin/python

class Graph :
    def __init__ (self) :
        self.edges = {}

    def add_edge (self, from_, to) :
        if from_ not in self.edges :
            self.edges[from_] = [to]
        else :
            self.edges[from_].append(to)

    def find_reachable_nodes (self, source_nodes) :
        pass
