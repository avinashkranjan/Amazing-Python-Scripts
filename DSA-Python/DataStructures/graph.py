"""
Graph Visualization

                member1--member5
                   |
        member3--member0--member2
                   |
                 member4


            |------city1----city3
            |        |       |
         city4----city2------|
                           city5


Graph Usage
    Facebook Friends Suggestion
        [m0 is friend of m1 & m5 is friend of m1; it is likely that m0 is friend of m5 too...
            FB will suggest m5 as friend suggestion to m0]
    Flight Routes : To find shortest path between two nodes
        [(city1,city2),(city1,city3),(city1,city4),
         (city2,city1),(city2,city4),(city2,city5),
         (city3,city1),(city3,city5),
         (city4,city1),(city4,city2),
         (city5,city2),(city5,city3)]
    Google Maps
    Internet
    E-commerce shopping Recommendation

Difference between TREE and GRAPH:
    In TREE, there is only one path between two nodes. GRAPH is a complex DS where two nodes can randomly be connected

"""

class Graph:
    def __init__(self, edges):
        self.edges = edges
        # Transform route tuple to route dictionary
        self.graph_dict = {}  # blank dictionary
        for start, end in self.edges:
            if start in self.graph_dict:  # element1 is already in dictionary
                self.graph_dict[start].append(end)  # add another element associated to element1 in graph_dictionary
            else:
                self.graph_dict[start] = [end]  # if element1 is not present, add it to graph_dictionary
        print("Graph dictionary: ", self.graph_dict)  # print route dictionary

    # get paths between start-point and end-point
    def getpath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:  # if one-way between one node, say Chennai; return []
            # Chennai is not as a starting point, so it has no route associated
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.getpath(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    # method to find shortest path between start-point and end-point
    def getShortestPath(self, start, end, path=[]):
        path = path + [start]

        # if starting-point and end-point are same
        if start == end:
            return path

        # If no path available from a point, return None
        if start not in self.graph_dict:
            return None

        # searching for shortest path
        shortest_path = None  # shortest path initialised
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.getShortestPath(node, end, path)
                if sp:
                    # if no shortest path is available; but in later iteration, we may have a path
                    # so check if it is shorter than original path (array of routes) or not
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp  # shortest path returned

        return shortest_path




if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    ''' start == end
    start = "Mumbai"
    end = "Mumbai"
    [op]: [['Mumbai']]'''

    ''' start not in self.graph_dict
    start = "Chennai"
    end = "Mumbai"
    [op]: []'''

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.getpath(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.getShortestPath(start,end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.getpath(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.getShortestPath(start,end))