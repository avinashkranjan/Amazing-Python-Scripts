'''
------------------------------------- Fleury's Algorithm -------------------------------------

Approach:-
1. Start with any vertex in the graph.

2. While there are unused edges in the graph, do the following steps:
    a. Choose any unused edge connected to the current vertex. It doesn't matter which one you choose.
    b. If removing the chosen edge doesn't disconnect the graph, go to the vertex at the other end of the chosen edge.
    c. If removing the chosen edge disconnects the graph, backtrack to the previous vertex that still has unused edges and choose a different edge.
    d. Repeat steps (a) to (c) until you can no longer choose any unused edges from the current vertex.

3. The algorithm terminates when you have traversed all the edges of the graph.

4. If all the vertices in the graph have even degrees, you will end up with an Eulerian circuit, which is a closed path that visits each edge exactly once.

5. If exactly two vertices in the graph have odd degrees, you will end up with an Eulerian path, which is a path that starts and ends at different vertices and visits each edge exactly once.
'''

# Program Starts
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    # This function removes edge source-destination from graph
    def removeEdge(self, source, destination):
        for index, key in enumerate(self.graph[source]):
            if key == destination:
                self.graph[source].pop(index)
        for index, key in enumerate(self.graph[destination]):
            if key == source:
                self.graph[destination].pop(index)

    # A DFS based function to count reachable vertices from destination
    def DFSCount(self, destination, visited):
        count = 1
        visited[destination] = True
        for i in self.graph[destination]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)
        return count

    # The function to check if edge source-destination can be considered as next edge in Euler Trail
    def isValidNextEdge(self, source, destination):
        # The edge source-destination is valid in one of the following two cases:

        # 1) If destination is the only adjacent vertex of source
        if len(self.graph[source]) == 1:
            return True
        else:
            '''
            2) If there are multiple adjacents, then source-destination is not a bridge
                    Do following steps to check if source-destination is a bridge

            2.a) count of vertices reachable from source'''
            visited = [False]*(self.V)
            count1 = self.DFSCount(source, visited)

            '''2.b) Remove edge (source, destination) and after removing the edge, count
				vertices reachable from source'''
            self.removeEdge(source, destination)
            visited = [False]*(self.V)
            count2 = self.DFSCount(source, visited)

            # 2.c) Add the edge back to the graph
            self.addEdge(source, destination)

            # 2.d) If count1 is greater, then edge (source, destination) is a bridge
            return False if count1 > count2 else True

    # Print Euler Trail starting from vertex source

    def printEulerUtil(self, source):
        # Recur for all the vertices adjacent to this vertex
        for destination in self.graph[source]:
            # If edge source-destination is not removed and it's a a valid next edge
            if self.isValidNextEdge(source, destination):
                print("%d-%d " % (source, destination)),
                self.removeEdge(source, destination)
                self.printEulerUtil(destination)

    '''The main function that print Eulerian Trail. It first finds an odd
degree vertex (if there is any) and then calls printEulerUtil()
to print the path '''

    def printEulerTrail(self):
        # Find a vertex with odd degree
        source = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                source = i
                break
        # Print Trail starting from odd vertex
        print("\n")
        self.printEulerUtil(source)


# Driver program
V = int(input("\nEnter the number of vertices in the graph: "))

g = Graph(V)

E = int(input("\nEnter the number of edges in the graph: "))

# Taking input from the user
print("\nEnter the edges in the format (source destination)")
for i in range(E):
    source = int(input(f"Source {i+1}: "))
    destination = int(input(f"Destination {i+1}: "))
    g.addEdge(source, destination)

# Printing the final result after analysing
print("\nResult of Fleury Algorithm: ", end="")
g.printEulerTrail()
print()
