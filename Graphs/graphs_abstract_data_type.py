import numpy as np
"""
Abstract Data types means functionality of different operation of such data type is
hidden from the user. Operation logics are hidden.
"""


class _Graphs:
    __slots__ = '_vertices', '_adj_matrix'

    def __init__(self, vertices):
        self._vertices = vertices
        self._adj_matrix = np.zeros((self._vertices, self._vertices))

    def add_edge(self, u, v, x=1):
        self._adj_matrix[u][v] = x

    def remove_edge(self, u, v):
        self._adj_matrix[u][v] = 0

    def exist_edge(self, u, v):
        return self._adj_matrix[u][v] != 0

    def count_vertices(self):
        return self._vertices

    def count_edges(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adj_matrix[i][j] != 0:
                    count += 1
        return count

    def display_vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def display_edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adj_matrix[i][j] != 0:
                    print("Vertix {} has edge at {} column ".format(i, j), end='\n')
            print('-' * 50)
        print()

    def in_degree(self, v):
        for i in range(self._vertices):
            if self._adj_matrix[i][v] != 0:
                print("Vertix {} has in_degree at {} column ".format(v, i), end='\n')
            print('-' * 50)
        print()

    def out_degree(self, v):
        for i in range(self._vertices):
            if self._adj_matrix[v][i] != 0:
                print("Vertix {} has out_degree at {} column ".format(v, i), end='\n')
            print('-' * 50)
        print()

    def display_adj_matrix(self):
        print(self._adj_matrix)
