"""
name: Dawson Dolansky
date: 4/20/2023

Max Clique Approximation Solution.

Code that provides an approximation solution to finding a Max Clique in Polynomial Time.
"""

def main():
    # read in input
    n = int(input())

    vertices = {v: {} for v in range(n)}
    for _ in range(n):
        v, *edges = input().split()

        for edge in edges:
            vertices[int(v)][int(edge)] = True


if __name__ == "__main__":
    main()
