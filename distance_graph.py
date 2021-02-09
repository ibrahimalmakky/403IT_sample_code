from graph import Graph

class Distance_Graph(Graph):
    
    def __init__(self):
        super().__init__()


    def add_node(self, node):
        self.map[node] = ([],[])


    def add_edge(self, node1, node2, distance):
        try:
            self.map[node1][0].append(node2)
            self.map[node1][1].append(distance)
            self.map[node2][0].append(node1)
            self.map[node2][1].append(distance)
        except:
            print("Make sure both nodes already exist in the graph.")


    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])


    def get_smallest_ind(self, my_list):
        smallest_ind = 0
        for i in range(1,len(my_list)):
            if my_list[i] < my_list[smallest_ind]:
                smallest_ind = i
        return smallest_ind 

    # A initial implementation of Dijkstra's algorithm
    def dijkstra(self, start, end):
        visited = []
        current_path = [start]
        current_node = start
        # x = 0
        while end not in current_path:
            # Mark the current node as visited
            visited.append(current_node)

            # Get the nodes that the current node is connected to
            connected_nodes = self.map[current_node]

            dead_end = True
            distances = ([],[])
            for i in range(0, len(connected_nodes[0])):
                node = connected_nodes[0][i]
                distance = connected_nodes[1][i]
                if node not in visited:
                    distances[0].append(node)
                    distances[1].append(distance)
                    dead_end = False
            print(distances)
            if dead_end:
                del current_path[-1]
                current_node = current_path[-1]
            else:
                closest_ind = self.get_smallest_ind(distances[1])
                closest_node = distances[0][closest_ind]
                current_node = closest_node
                current_path.append(current_node)
            print(current_path)
            
        return current_path


my_graph = Distance_Graph()
my_graph.add_nodes(["B","C","D","E","F","G","H","I"])
my_graph.add_edges([("B","C",5),("D","C",10),("D","E",5),("C","E",5),("F","E",10),("F","G",8),("G","H",5),("G","I",12),("H","I",5)])
print(my_graph.dijkstra("D","I"))