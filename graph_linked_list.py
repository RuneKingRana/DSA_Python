class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class Graph:
    def __init__(self, num_vertices):
        self.N = num_vertices
        self.adjList = [None for _ in range(self.N)]

    def add_edge(self, src, dest):
        new_node = Node(dest)
        new_node.next = self.adjList[src]
        self.adjList[src] = new_node

    def display(self):
        print("Adjacency List:")
        for i in range(self.N):
            print(f"{i}:", end=" ")
            temp = self.adjList[i]
            while temp:
                print(temp.vertex, end=" ")
                temp = temp.next
            print()

def main():
    N = int(input("Enter the number of vertices: "))
    graph = Graph(N)

    print("Enter the adjacency matrix:", end = " ")
    for i in range(N):
        row = [int(input()) for i in range(N)]
        for j in range(N):
            if row[j] == 1:
                graph.add_edge(i, j)

    graph.display()

if __name__ == "__main__":
    main()
