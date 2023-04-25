"""
name: Dawson Dolansky
date: 4/20/2023

Max Clique Optimal Solution.

Code that provides the exact solution to finding a Max Clique
"""
import random


def BronKerbosch_pivot(all_maximal_cliques, clique, possible_clique_additions, graph):
    """
    Maximal Clique Listing algorithm for finding all cliques that have reached their
    maximum size, through implementation of the Bron–Kerbosch algorithm with pivoting.

    :param graph: graph of vertices with their respective undirected edges stored in a dict
    :return:
    """
    # Maximal clique found when no more possible clique addition
    if len(possible_clique_additions) == 0:
        return all_maximal_cliques.append(clique)

    # Utilize a pivot vertex for finding additional clique additions
    pivot = possible_clique_additions.pop()
    possible_clique_additions.add(pivot) # no peek function
    for vertex in possible_clique_additions:
        if len(graph[pivot]) < len(graph[vertex]):
            pivot = vertex

    # iterate through the pivot and its non neighbors
    # P_sub_pivot_neighbors = P - N(pivot)
    P_sub_pivot_neighbors = filter(lambda v: v not in graph[pivot], possible_clique_additions)
    for v in P_sub_pivot_neighbors:
        """
        BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        
        Recurse through neighboring vertices of the current clique
        """
        # R: set of vertices found; Current Clique
        R = clique.union({v})

        # P: Set of possible clique vertex additions based on neighbors
        P = possible_clique_additions.intersection(set(graph[v]))

        # Not using X because it is just a mathematics proof
        BronKerbosch_pivot(all_maximal_cliques,
                           R,
                           P,
                           graph)

        # P := P \ {v}
        # Done through the filter iterator

def main():
    # read in input
    n_edges = int(input())

    graph = {}
    vertices = set()
    for _ in range(n_edges):
        u, v = input().split()

        if u not in graph:
            graph[u] = set()
            vertices.add(u)
        if v not in graph:
            graph[v] = set()
            vertices.add(v)

        graph[u].add(v)
        graph[v].add(u)

    if len(vertices) <= 1:
        if len(vertices) == 0:
            print('∅')
        else:
            print(vertices.pop())
        return

    # Find the all cliques
    maximal_cliques = []
    BronKerbosch_pivot(maximal_cliques, set(), vertices, graph)

    print(*list(max(maximal_cliques, key=len))) # Arbitrary first choice

if __name__ == "__main__":
    main()

