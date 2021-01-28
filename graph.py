class Graph:

    def __init__(self):
        self.map = {}

    def add_node(self, node):
        self.map[node] = []

    def add_edge(self, node1, node2):
        try:
            self.map[node1].append(node2)
            self.map[node2].append(node1)
        except:
            print("Make sure both nodes already exist in the graph.")
    
my_graph = Graph()
my_graph.add_node("E")
my_graph.add_node("F")
my_graph.add_edge("E", "F")
print(my_graph.map)