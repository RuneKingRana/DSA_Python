def display(graph, N):
    for i in range(N):
        print(f"{i}:", end=" ")
        for j in range(N):
            if graph[i][j] == 1:
                print(j, end=" ")
        print()

def main():
    N = int(input("Enter the number of vertices: "))

    print("Enter the adjacency matrix:", end = " ")
    graph = []
    for i in range(N):
        row = [int(input()) for i in range(N)]
        graph.append(row)

    print("Adjacency List:")
    display(graph, N)


if __name__ == "__main__":
    main()
