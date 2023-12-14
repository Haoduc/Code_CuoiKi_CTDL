import heapq  # Thư viện để sử dụng heap

# Lớp đại diện cho một cạnh trong đồ thị
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight  # Trọng số của cạnh
        self.start_vertex = start_vertex  # Đỉnh bắt đầu của cạnh
        self.target_vertex = target_vertex  # Đỉnh kết thúc của cạnh

# Lớp đại diện cho một đỉnh trong đồ thị
class Node:
    def __init__(self, name):
        self.name = name  # Tên của đỉnh
        self.visited = False  # Biến kiểm tra xem đỉnh đã được xét chưa
        self.predecessor = None  # Đỉnh trước đó trên đường đi ngắn nhất từ đỉnh bắt đầu
        self.adjacency_list = []  # Danh sách các cạnh kề với đỉnh
        self.min_distance = float('inf')  # Khoảng cách tối thiểu từ đỉnh bắt đầu đến đỉnh hiện tại

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance  # So sánh khoảng cách tối thiểu giữa hai đỉnh
    
# Triển khai thuật toán Dijkstra
class DijkstraAlgorithm:
    def __init__(self):
        self.heap = []  # Heap đối ứng để lưu trữ các đỉnh theo khoảng cách tối thiểu

    # Tính toán các đường đi ngắn nhất từ đỉnh bắt đầu đến tất cả các đỉnh khác
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0  # Đặt khoảng cách tối thiểu của đỉnh bắt đầu là 0
        heapq.heappush(self.heap, start_vertex)  # Đưa đỉnh bắt đầu vào heap

        while self.heap:  # Lặp cho đến khi heap rỗng
            actual_vertex = heapq.heappop(self.heap)  # Lấy đỉnh có khoảng cách tối thiểu ra khỏi heap

            for edge in actual_vertex.adjacency_list:  # Duyệt qua các cạnh kề với đỉnh hiện tại
                u = edge.start_vertex
                v = edge.target_vertex

                new_distance = u.min_distance + edge.weight  # Tính khoảng cách mới qua cạnh hiện tại

                # Nếu có một đường đi mới ngắn hơn đến đỉnh v, cập nhật thông tin của v
                if new_distance < v.min_distance:
                    v.predecessor = u  # Cập nhật đỉnh trước đó của v
                    v.min_distance = new_distance  # Cập nhật khoảng cách tối thiểu của v

                    heapq.heappush(self.heap, v)  # Đưa đỉnh v vào heap để xem xét tiếp

            actual_vertex.visited = True  # Đánh dấu đỉnh hiện tại đã được xét

    # In đường đi ngắn nhất đến đỉnh được chỉ định
    def get_shortest_path(self, vertex):
        print("Shortest path to vertex is: %s" % str(vertex.min_distance))  # In khoảng cách ngắn nhất đến đỉnh

        actual_vertex = vertex

        # Lặp qua các đỉnh trên đường đi ngắn nhất và in tên của chúng
        while actual_vertex is not None: 
            print("%s" % actual_vertex.name)  # In tên đỉnh
            actual_vertex = actual_vertex.predecessor  # Di chuyển đến đỉnh trước đó trong đường đi


if __name__ == "__main__":
    # Tạo các đỉnh và cạnh để biểu diễn đồ thị
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    # định nghĩa các cạnh khác
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(6, node8, node6)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # Thêm các cạnh vào danh sách kề của các đỉnh
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node2.adjacency_list.append(edge6)
    node8.adjacency_list.append(edge7)
    node8.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node5.adjacency_list.append(edge11)
    node6.adjacency_list.append(edge12)
    node6.adjacency_list.append(edge13)
    node3.adjacency_list.append(edge14)
    node3.adjacency_list.append(edge15)
    node4.adjacency_list.append(edge16)

    # Chạy thuật toán Dijkstra và in đường đi ngắn nhất đến một đỉnh cụ thể
    algorithm = DijkstraAlgorithm()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node7)
