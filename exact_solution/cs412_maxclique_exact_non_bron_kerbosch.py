"""
name: Dawson Dolansky
date: 4/20/2023

Max Clique Optimal Solution.

Code that provides the exact solution to finding a Max Clique
"""
import random
from time import time
from itertools import chain, combinations

def exact_solution(vertices, graph):
    """
    Find all subsets, search every subset for being a clique, get the largest clique

    :param graph: graph of vertices with their respective undirected edges stored in a dict
    :return:
    """
    # Generate every subset (n!), where each subset is implicitly complete
    subsets = chain.from_iterable(combinations(vertices, size) for size in range(len(vertices) + 1))

    # Keep only subsets that are complete
    cliques = []
    for subset in subsets:
        is_complete = True
        if len(subset) <= 2:
            if len(cliques) == 0 and len(subset) > 1:
                cliques.append(subset)
            continue
        else:
            for i in range(0, len(subset) - 1):
                for j in range(i, len(subset) - 1):
                    u, v = subset[i], subset[j+1]
                    if v not in graph[u]:
                        is_complete = False
                        break

        if is_complete:
            cliques.append(subset)

    # return the largest clique
    return max(cliques, key=len)


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
    before = time()
    max_clique = exact_solution(vertices, graph)
    after = time()

    print(*max_clique)

    print("\nruntime: ", after - before)

if __name__ == "__main__":
    main()
