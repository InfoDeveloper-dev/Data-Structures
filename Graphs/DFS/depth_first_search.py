import numpy as np

"""
Abstract Data types means functionality of different operation of such data type is
hidden from the user. Operation logics are hidden.
"""


class _Graphs:
    __slots__ = '_vertices', '_adj_matrix', '_visited'

    def __init__(self, vertices):
        self._vertices = vertices
        self._adj_matrix = np.zeros((self._vertices, self._vertices))
        self._visited = [0] * self._vertices

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
        print()

    def in_degree(self, v):
        array = np.zeros((self._vertices, self._vertices))
        for i in range(self._vertices):
            if self._adj_matrix[i][v] != 0:
                print("Vertix {} has in_degree from {} column ".format(v, i), end='\n')
                array[i][v] = 1

        if not array.any():
            print("Vertex {} has no in degree.......".format(v))
        print()

    def out_degree(self, v):
        array = np.zeros((self._vertices, self._vertices))
        for i in range(self._vertices):
            if self._adj_matrix[v][i] != 0:
                print("Vertix {} has out_degree at {} column ".format(v, i), end='\n')
                array[i][v] = 1

        if not array.any():
            print("Vertex {} has no out degree.......".format(v))
        print()

    def display_adj_matrix(self):
        print(self._adj_matrix)

    def depth_first_search(self, s):
        i = s
        if self._visited[i] == 0:
            print(i)
            self._visited[i] = 1
            for j in range(self._vertices):
                if self._adj_matrix[i][j] == 1 and self._visited[j] ==0:
                    self.depth_first_search(j)


G = _Graphs(4)
print("adjanceny matrix before any edges: \n", G._adj_matrix)
G.add_edge(u=0, v=1)
G.add_edge(u=1, v=2)
G.add_edge(u=0, v=3)
G.add_edge(u=2, v=3)
print("adjanceny matrix after adding edges: \n", G._adj_matrix)
print("Edges in the graph are: {}".format(G.count_edges()))
G.display_edges()
print("check if edge exit between two vertex:", G.exist_edge(2, 0))
G.in_degree(0)
G.in_degree(3)
G.out_degree(3)
print("Result from Breadth First Search is as below......")
G.depth_first_search(0)
