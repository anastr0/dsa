
###################################################################################
# Adjascency matrix

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.vertices = set([i for i in range(size)])
    
    def display(self):
        print("Adj matrix", self.vertices)
        for row in self.adj_matrix:
            print(*row)

    def set_adj_matrix(self, mat):
        if len(mat) == len(self.adj_matrix) and \
            len(mat[0]) == len(self.adj_matrix[0]):
            self.adj_matrix = mat

    def DFS(self, i, visited):
        print(i)
        visited.add(i)

        for j in range(self.size):
            if self.adj_matrix[i][j] == 1 and j not in visited:
                self.DFS(j, visited)


    def dfs(self, v):
        print("DFS")
        visited = set()
        self.DFS(0, visited)

    def bfs(self, v):
        print("BFS")
        
        queue = [v]
        marked = set(queue)
        while len(queue) > 0:
            i = queue.pop(0)
            print(i)

            for j in range(self.size):
                if self.adj_matrix[i][j] == 1 and j not in marked:
                    queue.append(j)
                    marked.add(j)
    
    def shortest_path(self, v):
        print("Shortest path from v1 to all vertices")

        sptSet = set()
        Distance = [float('inf')]*self.size
        Distance[v] = 0

        while len(sptSet) < self.size:
            # wrong
            # read https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
            # for more info
            sptSet.add(v)
            v += 1




vertexData = ['A', 'B', 'C', 'D']

# adjacency_matrix = [
#     [0, 1, 1, 1],  # Edges for A
#     [1, 0, 1, 0],  # Edges for B
#     [1, 1, 0, 0],  # Edges for C
#     [1, 0, 0, 0]   # Edges for D
# ]

adjacency_matrix = [
    [0, 1, 0, 1],  # Edges for A
    [1, 0, 0, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

g = Graph(4)

print(g.vertices)
print(g.size)
g.display()
g.set_adj_matrix(adjacency_matrix)
g.display()

g.dfs(0)
g.bfs(0)

