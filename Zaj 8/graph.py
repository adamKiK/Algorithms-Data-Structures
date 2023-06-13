class Vertex:
    def __init__(self, label="New_Vertex"):
        self.label = label
        self.neighbors = []

    def set_label(self, new_label):
        self.label = new_label

    def append_vertex_neighbors(self, neighbor_labels):
        if len(neighbor_labels) > 0:
            for i in neighbor_labels:
                self.neighbors.append(i)

    def get_label(self):
        return self.label


class Graph:
    def __init__(self):
        self.vertices = []

    def append_vertex(self, new_vertex_label, *neighbor_labels):
        new_vertex = Vertex()
        new_vertex.set_label(new_vertex_label)
        new_vertex.append_vertex_neighbors(neighbor_labels)
        self.vertices.append(new_vertex)

    def remove_vertex(self, vertex_label):
        for i in self.vertices:
            if i.get_label(vertex_label) == vertex_label:
                self.vertices.remove(i)
        self.remove_vertex_from_neighbors(vertex_label)

    def remove_vertex_from_neighbors(self, vertex_label):
        for i in self.vertices:
            for j in i.neighbors:
                if j == vertex_label:
                    i.neighbors.remove(j)

    def represent_adjacency_list(self):
        for i in self.vertices:

if __name__ == "__main__":
    graph = Graph()

    while True:
        usr_input = input("1. Add vertex\n2. Remove vertex\n3. Adjacency List\n0. Exit\nEnter: ")
        if usr_input == "1":
            vertex_name = input("Enter vertex label: ")
            vertex_neighbors = input("Enter vertex neighbors: ")
            graph.append_vertex(vertex_name, vertex_neighbors)
        elif usr_input == "2":
            vertex_name = input("Enter vertex name: ")
            graph.remove_vertex(vertex_name)
        elif usr_input == "3":
            graph.represent_adjacency_list()
        else:
            break
