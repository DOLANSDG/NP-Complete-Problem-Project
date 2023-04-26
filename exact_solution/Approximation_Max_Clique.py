"""
name: Dawson Dolansky
date: 4/20/2023

Max Clique Approximation Solution.

Code that provides an approximation solution to finding a Max Clique in Polynomial Time.
Utilization of the Bron–Kerbosch algorithm.
https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
"""


def approximation_algorithm(all_maximal_cliques, clique, possible_clique_additions, graph):
    """
    Breadth First Search from a node to find connected and complete vertices

    :param graph: graph of vertices with their respective undirected edges stored in a dict
    :return:
    """
    # Maximal clique found when no more possible clique addition
    if len(possible_clique_additions) == 0:
        return all_maximal_cliques.append(clique)

    # Utilize a pivot vertex for finding additional clique additions
    pivot = possible_clique_additions.pop()
    possible_clique_additions.add(pivot)  # no peek function
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
    n = int(input())

    graph = [None for _ in range(n)]
    for _ in range(n):
        v, *edges = input().split()

        for edge in edges:
            graph[int(v)] = [int(val) for val in edges]

    # Find the all cliques
    maximal_cliques = []
    approximation_algorithm(maximal_cliques, set(), set(range(n)), graph)

    max_clique = max(maximal_cliques, key=len)
    print(max(maximal_cliques, key=len))  # Arbitrary first choice


if __name__ == "__main__":
    main()
