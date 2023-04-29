"""
name: Dawson Dolansky
date: 4/20/2023

Max Clique Optimal Solution.

Code that provides the exact solution to finding a Max Clique
"""
import random


def main():
    n_vertices = int(input()) # n vertices

    vertices = set()
    for i in range(n_vertices):
        vertices.add(i)

    # generate random amount of edges less than or equal to that of a complete graph, based on
    # boolean
    edges = set()
    for u in vertices:
        for v in vertices:
            if bool(random.getrandbits(1)) and u != v:
                pair = f"{min(u, v)} {max(u, v)}"
                edges.add(pair)

    with open(f'gen_{len(edges)}_edges.txt', 'w') as file:
        file.write(f'{len(edges)}\n')

        for edge in edges:
            file.write(edge + '\n')

if __name__ == "__main__":
    main()
