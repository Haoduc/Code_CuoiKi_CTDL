

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight  # Trọng số của cạnh
        self.start_vertex = start_vertex  # Đỉnh bắt đầu của cạnh
        self.target_vertex = target_vertex  # Đỉnh kết thúc của cạnh

class Node:
    def __init__(self, name):
        self.name = name  # Tên của đỉnh
        self.adjacency_list = []  # Danh sách các cạnh kề với đỉnh
        self.predecessor = None  # Đỉnh trước đó trên đường đi ngắn nhất từ đỉnh bắt đầu
        self.min_distance = float('inf')  # Khoảng cách tối thiểu từ đỉnh bắt đầu đến đỉnh hiện tại

class BellmanFordAlgorithm:
    def __init__(self, vertex_list, edge_list, start_vertex):
        self.vertex_list = vertex_list  # Danh sách các đỉnh trong đồ thị
        self.edge_list = edge_list  # Danh sách các cạnh trong đồ thị
        self.start_vertex = start_vertex  # Đỉnh bắt đầu
        self.has_cycle = False  # Biến kiểm tra có chu trình âm hay không

    def find_shortest_path(self):
        # Khởi tạo khoảng cách nhỏ nhất từ đỉnh bắt đầu đến chính nó là 0
        self.start_vertex.min_distance = 0

        # Thuật toán Bellman-Ford
        for _ in range(len(self.vertex_list) - 1):  # Lặp qua tất cả các đỉnh
            for edge in self.edge_list:  # Lặp qua tất cả các cạnh
                u = edge.start_vertex
                v = edge.target_vertex  # Đỉnh kết thúc của cạnh

                dist = u.min_distance + edge.weight  # Tính khoảng cách mới qua cạnh hiện tại

                # Bước thư giãn: Cập nhật khoảng cách nếu tìm thấy một đường đi ngắn hơn
                if dist < v.min_distance:
                    v.predecessor = u  # Cập nhật đỉnh trước đó của v
                    v.min_distance = dist  # Cập nhật khoảng cách tối thiểu của v

        # Kiểm tra có chu trình âm sau khi thư giãn tất cả các cạnh
        for edge in self.edge_list:
            if self.check_cycle(edge):  # Nếu có chu trình âm
                print("Phát hiện chu trình âm...")  # In thông báo
                return

    def check_cycle(self, edge):
        # Kiểm tra xem có chu trình âm hay không và đặt cờ nếu có
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:  # Nếu có chu trình âm
            self.has_cycle = True  # Đặt cờ has_cycle là True
            return True
        else:
            return False

    def get_shortest_path(self, vertex):
        # In đường đi ngắn nhất hoặc thông báo về chu trình âm
        if not self.has_cycle:  # Nếu không có chu trình âm
            print("Đường đi ngắn nhất có giá trị: ", vertex.min_distance)  # In khoảng cách ngắn nhất đến đỉnh
            node = vertex

            while node is not None:  # Lặp qua các đỉnh trên đường đi ngắn nhất
                print(node.name)  # In tên đỉnh
                node = node.predecessor  # Di chuyển đến đỉnh trước đó trong đường đi
        else:
            print('Đồ thị G(V, E) có chu trình âm...')  # In thông báo về chu trình âm

if __name__ == '__main__':
    # Tạo các đỉnh và cạnh để biểu diễn đồ thị
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(9, node1, node5)
    edge3 = Edge(4, node2, node5)
    edge4 = Edge(12, node2, node3)
    edge5 = Edge(7, node2, node4)
    edge6 = Edge(3, node3, node4)
    edge7 = Edge(1, node3, node6)
    edge8 = Edge(9, node4, node7)
    edge9 = Edge(6, node5, node3)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(2, node6, node7)
    edge12 = Edge(6, node7, node3)

    # Thêm các cạnh vào danh sách kề của các đỉnh
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node3.adjacency_list.append(edge6)
    node3.adjacency_list.append(edge7)
    node4.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node6.adjacency_list.append(edge11)
    node7.adjacency_list.append(edge12)

    vertices = [node1, node2, node3, node4, node5, node6, node7]  # Danh sách các đỉnh
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12]  # Danh sách các cạnh

    algorithm = BellmanFordAlgorithm(vertices, edges, node1)  # Khởi tạo thuật toán với danh sách đỉnh, danh sách cạnh và đỉnh bắt đầu
    algorithm.find_shortest_path()  # Tìm đường đi ngắn nhất
    algorithm.get_shortest_path(node7)  # In đường đi ngắn nhất đến đỉnh node7
