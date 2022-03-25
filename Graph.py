from queue import PriorityQueue


class Graph:
    overview = {0: ['Yio Chu Kang Sports and Recreation Centre Drop Off Point', 1.38367, 103.84627],
                1: ['Avenue 9 to Yio Chu Kang Sports and Recreation Centre Junction', 1.3842, 103.8453],
                2: ['Avenue 9 to Avenue 6 Junction', 1.38394, 103.84329],
                3: ['Avenue 6 to Presbyterian High School Junction', 1.38209, 103.84394],
                4: ['Presbyterian High School Drop Off Point', 1.38241, 103.84336],
                5: ['Yio Chu Kang Mrt Station Drop Off Point', 1.38147, 103.84489],
                6: ['Junction of Avenue 8 to Yio Chu Kang Mrt Station Drop Off Point', 1.38078, 103.84524],
                7: ['Avenue 6 to Avenue 8 Junction', 1.38079, 103.84426],
                8: ['Anderson Serangoon JC Drop off', 1.3794, 103.84457],
                9: ['Junction of Avenue 8 to Avenue 9', 1.37849, 103.84746],
                10: ['Junction of Avenue 9 to Nanyang Polytechnic Drop Off Point', 1.37939, 103.84781],
                11: ['Nanyang Polytechnic Drop Off Point', 1.37982, 103.84822],
                12: ['Junction of Avenue 9 to SIT Drop Off Poinlt', 1.3769, 103.84864],
                13: ['SIT Drop Off Point', 1.37728, 103.84915],
                14: ['Avenue 5 to Avenue 6 Junction', 1.37718, 103.84508],
                15: ['Junction of Avenue 6 to Ang Mo Kio Library', 1.37486, 103.84511],
                16: ['Ang Mo Kio Library Drop Off Point', 1.37488, 103.84531],
                17: ['Avenue 6 to Avenue 3 Junction', 1.36917, 103.84568],
                18: ['Junction of Avenue 3 to AMK Hub Drop Off Point', 1.36888, 103.84794],
                19: ['AMK Hub Drop Off Point', 1.36901, 103.84796],
                20: ['Junction of Avenue 5 and Avenue 8', 1.37666, 103.84754],
                21: ['Junction of Avenue 8 and Central 3', 1.37529, 103.84781],
                22: ['Junction of Central 3 and Grandeur 8', 1.3752, 103.84711],
                23: ['Junction of Avenue 8 to Jubilee Square', 1.37203, 103.84829],
                24: ['Jubilee Square Drop Off Point', 1.37186, 103.8481],
                25: ['Avenue 8 to Avenue 3 Junction', 1.3691, 103.84962],
                26: ['Avenue 3 to Street 42 Junction', 1.36966, 103.85215],
                27: ['Avenue 3 to Street 43 Junction', 1.36941, 103.85543],
                28: ['Street 43 to Avenue 10 Junction', 1.36705, 103.85658],
                29: ['Avenue 10 to Street 44 Junction', 1.36788, 103.85677],
                30: ['Street 44 to Chek Sian Tng Temple Junction', 1.3679, 103.85718],
                31: ['Chek Sian Tng Temple Drop Off Point', 1.36804, 103.85709],
                32: ['Junction of Avenue 5 and Street 53', 1.376220, 103.850930],
                33: ['Junction of Street 53 and Anderson Secondary School', 1.37512, 103.85087],
                34: ['Anderson Secondary School Drop Off Point', 1.375, 103.85109],
                35: ['Avenue 5 to AMK Drive Junction', 1.37595, 103.85457],
                36: ['Junction of AMK Drive to ITE Central Drop Off Point', 1.37748, 103.8554],
                37: ['ITE Central Drop Off Point', 1.37724, 103.85547],
                38: ['Avenue 5 to Avenue 10 Junction', 1.37571, 103.85474],
                39: ['Avenue 10 to Cheng San Market Junction', 1.37365, 103.85541],
                40: ['Cheng San Market Drop Off Point', 1.37312, 103.85479]}
    allEdges = {0: [0, 1, 178],
                1: [1, 2, 226],
                2: [2, 3, 219],
                3: [3, 4, 192],
                4: [3, 7, 148],
                5: [7, 6, 108],
                6: [6, 5, 92],
                7: [6, 9, 363],
                8: [9, 10, 126],
                9: [10, 11, 77],
                10: [10, 12, 310],
                11: [12, 13, 81],
                12: [7, 8, 158],
                13: [8, 14, 254],
                14: [14, 15, 259],
                15: [15, 16, 22],
                16: [15, 17, 636],
                17: [17, 18, 254],
                18: [18, 19, 14],
                19: [14, 20, 280],
                20: [20, 21, 155],
                21: [21, 22, 78],
                22: [21, 23, 367],
                23: [23, 24, 29],
                24: [23, 25, 358],
                25: [25, 26, 289],
                26: [26, 27, 377],
                27: [27, 28, 405],
                28: [28, 29, 95],
                29: [29, 30, 45],
                30: [30, 31, 19],
                31: [20, 32, 380],
                32: [32, 33, 110],
                33: [33, 34, 34],
                34: [32, 35, 407],
                35: [35, 36, 210],
                36: [36, 37, 25],
                37: [35, 38, 32],
                38: [38, 39, 248],
                39: [39, 40, 94]}

    def __init__(self, num_of_vertices):
        # set the number of vertices it has i.e. how many connections
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        # initialises the graph
        for each_edge in range(len(self.allEdges.keys())):
            value_list = self.allEdges[each_edge]
            self.add_edge(value_list[0], value_list[1], value_list[2])

    # sets the connected node's weight/distance
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, graph, start_vertex, end_vertex):
        self.starting_point = start_vertex
        self.end_point = end_vertex
        self.shortest_Path = []
        D = {v: float('inf') for v in range(graph.v)}
        D[start_vertex] = 0
        self.parent = {v: int(-1) for v in range(graph.v)}

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)

            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
                            self.parent[neighbor] = current_vertex

        return D

    def getSolutions(self, mode, D):
        if mode == 1:  # returns shortest path
            self.pathSolution(self.parent, self.end_point)
            return self.shortest_Path

        if mode == 2:  # returns full Solution
            self.printSolution(D, self.parent)

        if mode == 3:  # returns nearby nodes
            self.getRadiusNodes(D)
            return self.radiusNodes

        if mode == 4:  # shows shortest distance from starting point to every other nodes.
            self.getAllPath(D, self.parent)

    def printPath(self, parent, j):  # functions that prints out shortest route taken recursively
        # Base Case : If j is source
        if parent[j] == -1:
            print(j, end=" ")
            return
        self.printPath(parent, parent[j])
        print(j, end=" ")

    def pathSolution(self, parent, j):
        # Base Case : If j is source
        if parent[j] == -1:
            self.shortest_Path.append(j)
            return
        self.pathSolution(parent, parent[j])
        self.shortest_Path.append(j)

    def printSolution(self, dist, parent):
        src = self.starting_point
        print("Vertex \t\tDistance from Source\tPath")
        print("\n%d --> %d \t\t%d \t\t" % (src, self.end_point, dist[self.end_point]), end=" ")
        self.printPath(parent, self.end_point)

    def getAllPath(self, dist, parent):
        src = self.starting_point
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(0, len(dist)):
            print("\n%d --> %d \t\t%d \t\t" % (src, i, dist[i]), end=" ")
            self.printPath(parent, i)

    def getRadiusNodes(self, dist):  # this function returns all nearby nodes based on radius set.
        src = self.starting_point
        self.radiusNodes = []
        for i in range(0, len(dist)):  # iterates through the whole distance list generated by dijkstra
            if dist[i] < 1000:  # radius set = 1000
                self.radiusNodes.append(i)
