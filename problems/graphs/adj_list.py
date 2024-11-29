class Vertex:
    def __init__(self, item=None):
        self.item = item
        self.neighbours = set()

class Graph:
    """Adjascency list repr"""
    def __init__(self, data=[]):
        self.vertices = {val: Vertex(val) for val in data}
    
    def add_vertex(self, val):
        if val in self.vertices:
            print("Val exists")
        else:
            node = Vertex(val)
            self.vertices[val] = node
    
    def add_edge(self, val1, val2):
        if val1 in self.vertices and \
            val1 in self.vertices:
            node1 = self.vertices[val1]
            node2 = self.vertices[val2]
            node1.neighbours.add(node2)
            node2.neighbours.add(node1)
        else:
            print("can't add edge, either of nodes", val1, val2, "not found")
    
    def DFS_graph(self, vertex, visited):
        if vertex == None:
            return
        print(vertex.item)
        visited.add(vertex)
        for neighbour in vertex.neighbours:
            if neighbour not in visited:
                self.DFS_graph(neighbour, visited)

    def dfs(self, v):
        root = self.vertices[v]
        visited = set()
        self.DFS_graph(root, visited)
    
    def bfs(self, v):
        root = self.vertices[v]

        marked = set()
        queue = [root]

        while len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex.item)

            for neighbour in vertex.neighbours:
                if neighbour not in marked:
                    queue.append(neighbour)
                    marked.add(neighbour)
        

        
    

g = Graph([1,2,3,4,5])

print(g.vertices.keys())

g.add_vertex(7)
g.add_vertex(10)
g.add_edge(7,10)
g.add_edge(1,2)
g.add_edge(1,5)
g.add_edge(5,2)
g.add_edge(2,4)
g.add_edge(7,2)
g.add_edge(11,10)

print(g.vertices.keys())

g.dfs(1)
print("BFS")
g.bfs(1)




            
