"""
name: Dawson Dolansky
date: 4/20/2023

Max Clique Approximation Solution.

Code that provides an approximation solution to finding a Max Clique in Polynomial Time.
Utilization of the Bron–Kerbosch algorithm.
https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
"""
import queue


def whatever_first_search(graph, bag, visited_vertices, isv):
    found_cliques = {}
    # O(n)
    while not bag.empty():
        u, parent_clique_members = bag.get()
        if u not in visited_vertices:
            visited_vertices.add(u)
            # Adjust clique
            # O(n)
            adjusted_clique = filter(lambda v: v not in graph[u], parent_clique_members.copy())
            for v in adjusted_clique:
                if v != u and v != isv:
                    parent_clique_members.remove(v)
            # DFS stack additions ; Same as graph[u] excluding non-clique members
            # O(n)
            for v in parent_clique_members:
                bag.put((v, parent_clique_members))

        # Check if all clique members are visited ; Check if clique found
        # O(n,m)
        if visited_vertices == visited_vertices.intersection(parent_clique_members):
            clique_key = str(parent_clique_members)
            if clique_key not in found_cliques:
                found_cliques[clique_key] = list(parent_clique_members)

    # The clique has been found in clique_members
    return found_cliques

def approximation_algorithm(all_maximal_cliques, vertices, graph):
    """
    Breadth First Search from a node to find connected and complete vertices

    :param graph: graph of vertices with their respective undirected edges stored in a dict
    :return:
    """
    # Get an independent set of vertices that are of higher degree first
    # O(n^3log(n))
    independent_set = set()
    for u in sorted(graph, key=lambda u: len(graph[u]), reverse=True):
        # utilized stack overflow for implementation of this sort
        # https://stackoverflow.com/questions/16868457/python-sorting-dictionary-by-length-of-values
        independent = True
        for v in graph[u]:
            if v in independent_set:
                independent = False
        if independent:
            independent_set.add(u)

    # n^3
    for u in independent_set:
        # O(n) worst case (chain graph)

        for v in graph[u]:
            # Worst case overall if half of vertices, with O(n) added to outer scope

            # Set of visited vertices ; O(1) access time
            visited_vertices = set()
            visited_vertices.add(u)

            # bag for stack
            possible_clique_members = graph[u].copy()
            possible_clique_members.add(u)
            bag = queue.LifoQueue()
            bag.put((v, possible_clique_members))

            # Find a maximal clique starting from (u,v)
            # O(n^2)
            cliques_found = whatever_first_search(graph, bag, visited_vertices, u)
            all_maximal_cliques += cliques_found.values()

    # All cliques have been found and added to maximal_clique
    return


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
    # n^3log(n)
    approximation_algorithm(maximal_cliques, vertices, graph)

    print(*list(max(maximal_cliques, key=len)))  # Arbitrary first choice


if __name__ == "__main__":
    main()
