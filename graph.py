class Graph:

    def __init__(self):
        self.map = {}


    def add_node(self, node):
        self.map[node] = []


    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)


    def add_edge(self, node1, node2):
        try:
            self.map[node1].append(node2)
            self.map[node2].append(node1)
        except:
            print("Make sure both nodes already exist in the graph.")


    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])


    # Depth first search implementation
    def depth_first_search(self, start, end):
        visited = []
        current_path = [start]
        current_node = start
        while current_node != end:
            # Mark the current node as visited
            visited.append(current_node)
            # Get the nodes that the current node is connected to
            connected_nodes = self.map[current_node]
            # Check the first node the current node is connected but has not been visited
            dead_end = True
            for connected_node in connected_nodes:
                if connected_node not in visited:
                    current_node = connected_node
                    dead_end = False
                    break
            if dead_end:
                del current_path[-1]
                current_node = current_path[-1]
            else:
                current_path.append(current_node)
            print(current_path)
        
        # Refine the current path
        for i in range(0, len(current_path)-2):
            for j in range(i+2, len(current_path)):
                if current_path[j] in self.map[current_path[i]]:
                    del current_path[i+1:j]
                    break
        print(current_path)
                     

    def find_shortest_path(self, start, end):
        pass


my_graph = Graph()
my_graph.add_nodes(["C","D","E","F","G","H","I"])
my_graph.add_edges([("E", "C"),("D", "C"),("D", "E"),("E", "F"),("F", "G"),("G", "H"),("H", "I"),("G","I")])
# print(my_graph.map)
# my_graph.depth_first_search("D","I")