"""
name: Dawson Dolansky
date: 4/20/2023

Max Clique Optimal Solution.

Code that provides the exact solution to finding a Max Clique
"""
import random


def BronKerbosch_pivot(all_maximal_cliques, clique, possible_clique_members, graph):
    """
    Maximal Clique Listing algorithm for finding all cliques that have reached their
    maximum size, through implementation of the Bron–Kerbosch algorithm with pivoting.

    :param graph: graph of vertices with their respective undirected edges stored in a dict
    :return:
    """
    # A clique is a complete subgraph of the graph
    # To find all maximal cliques, we must utilize every possible subgraph of the vertices

    # Maximal clique found when no more possible clique members
    if len(possible_clique_members) == 0:
        return all_maximal_cliques.append(clique)

    # Choose the next pivot vertex as the highest degree vertex
    pivot = possible_clique_members.pop()
    possible_clique_members.add(pivot) # no peek function
    for vertex in possible_clique_members:
        if len(graph[pivot]) < len(graph[vertex]):
            pivot = vertex

    # For each vertex that is either the pivot or not a neighbor
    P = filter(lambda v: v not in graph[pivot], possible_clique_members)
    for v in P:
        # BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        BronKerbosch_pivot(all_maximal_cliques,
                           clique.union({v}),
                           possible_clique_members.intersection(set(graph[v])),
                           graph)

        # P := P \ {v}
        possible_clique_members.remove(v)

def main():
    # read in input
    n = int(input())

    graph = [None for _ in range(n)]
    for _ in range(n):
        v, *edges = input().split()

        for edge in edges:
            graph[int(v)] = [int(val) for val in edges]

    # Find the all cliques
    maximal_cliques = []
    BronKerbosch_pivot(maximal_cliques, set(), set(range(n)), graph)

    print(maximal_cliques)

if __name__ == "__main__":
    main()

