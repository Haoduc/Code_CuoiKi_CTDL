import math  # Thư viện hỗ trợ các hàm toán học

class Node(object):

    def __init__(self, name):
        # Lớp Node biểu diễn một đỉnh trong đồ thị
        self.name = name  # Tên của đỉnh
        self.predecessor = None  # Đỉnh trước đó trên đường đi ngắn nhất từ đỉnh bắt đầu
        self.adjacency_list = []  # Danh sách để lưu trữ các cạnh đi ra từ đỉnh này
        self.min_distance = float('inf')  # Khoảng cách tối thiểu từ đỉnh bắt đầu

class Edge(object):

    def __init__(self, weight, start_vertex, target_vertex):
         # Lớp Edge biểu diễn một cạnh hướng trong đồ thị
        self.weight = weight  # Trọng số (chi phí) của cạnh
        self.start_vertex = start_vertex  # Đỉnh xuất phát của cạnh
        self.target_vertex = target_vertex  # Đỉnh đích của cạnh
        

class BellmanFord(object):

    def __init__(self, vertex_list, edge_list, start_vertex):
        # Lớp BellmanFord để tìm đường đi ngắn nhất trong một đồ thị
        self.vertex_list = vertex_list  # Danh sách các đỉnh trong đồ thị
        self.edge_list = edge_list  # Danh sách các cạnh trong đồ thị
        self.start_vertex = start_vertex  # Đỉnh xuất phát cho việc tính toán đường đi ngắn nhất
        self.cycle_list = []  # Danh sách để lưu trữ các đỉnh trong chu trình âm
        self.has_cycle = False  # Cờ để chỉ ra sự tồn tại của chu trình âm


    def calculate_shortest_path(self):
         # Tính toán đường đi ngắn nhất bằng thuật toán Bellman-Ford
        self.start_vertex.min_distance = 0  # Đặt khoảng cách tối thiểu từ đỉnh bắt đầu đến chính nó là 0

         # Làm giảm căng các cạnh để tìm ra đường đi ngắn nhất
        for _ in range(len(self.vertex_list) - 1):  # Lặp qua tất cả các đỉnh
            for edge in self.edge_list:  # Lặp qua tất cả các cạnh
                u = edge.start_vertex
                v = edge.target_vertex  # Đỉnh đích của cạnh
                dist = u.min_distance + edge.weight  # Tính khoảng cách mới qua cạnh hiện tại

                # Cập nhật khoảng cách tối thiểu nếu tìm thấy một đường đi ngắn hơn
                if dist < v.min_distance:
                    v.min_distance = dist
                    v.predecessor = u  # Cập nhật đỉnh trước đó của v

        # Kiểm tra chu trình âm
        for edge in self.edge_list:
            if self.check_cycle(edge):  # Nếu có chu trình âm
                print("Negative cycle detected...")  # In thông báo

                vertex = edge.start_vertex

                while vertex is not edge.target_vertex:  # Lặp qua các đỉnh trong chu trình âm
                    self.cycle_list.append(vertex)  # Thêm đỉnh vào danh sách chu trình
                    vertex = vertex.predecessor  # Di chuyển đến đỉnh trước đó trong chu trình

                self.cycle_list.append(edge.target_vertex)  # Thêm đỉnh đích của cạnh vào danh sách chu trình

                for v in self.cycle_list:  # In tên các đỉnh trong chu trình
                    print(v.name)

                return
            
    def check_cycle(self, edge):
        # Kiểm tra xem có chu trình âm hay không
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:  # Nếu có chu trình âm
            self.has_cycle = True  # Đặt cờ has_cycle là True
            return True
        else:
            return False
        
    
    def get_shortest_path_to(self, target_vertex):
        # In ra đường đi ngắn nhất đến một đỉnh đích
        if not self.has_cycle:  # Nếu không có chu trình âm

            print("Shortest path exists with value: ", target_vertex.min_distance)  # In khoảng cách ngắn nhất đến đỉnh
            node = target_vertex  # Corrected variable name

            while node is not None:  # Lặp qua các đỉnh trên đường đi ngắn nhất
                print("%s " % node.name)  # In tên đỉnh
                node = node.predecessor  # Di chuyển đến đỉnh trước đó trong đường đi
        else:
            print("No shortest path because of the negative cycle...")  # In thông báo về chu trình âm

if __name__ == '__main__':
    # Ví dụ sử dụng thuật toán BellmanFord với đồ thị trao đổi tiền tệ

    # Tạo các đỉnh cho các loại tiền tệ khác nhau
    node0 = Node("USD")
    node1 = Node("EUR")
    node2 = Node("GBP")
    node3 = Node("CHF")
    node4 = Node("CAD")

    # Tạo các cạnh biểu diễn tỷ giá hối đoái giữa các loại tiền tệ
    edge1 = Edge(-1 * math.log(0.741), node0, node1)
    edge2 = Edge(-1 * math.log(0.657), node0, node2)
    edge3 = Edge(-1 * math.log(0.061), node0, node3)
    edge4 = Edge(-1 * math.log(0.005), node0, node4)

    edge5 = Edge(-1 * math.log(1.349), node1, node0)
    edge6 = Edge(-1 * math.log(0.888), node1, node2)
    edge7 = Edge(-1 * math.log(1.433), node1, node3)
    edge8 = Edge(-1 * math.log(1.366), node1, node4)

    edge9 = Edge(-1 * math.log(1.521), node2, node0)
    edge10 = Edge(-1 * math.log(1.126), node2, node1)
    edge11 = Edge(-1 * math.log(1.614), node2, node3)
    edge12 = Edge(-1 * math.log(1.538), node2, node4)

    edge13 = Edge(-1 * math.log(0.942), node3, node0)
    edge14 = Edge(-1 * math.log(0.698), node3, node1)
    edge15 = Edge(-1 * math.log(0.619), node3, node2)
    edge16 = Edge(-1 * math.log(0.953), node3, node4)

    edge17 = Edge(-1 * math.log(0.995), node4, node0)
    edge18 = Edge(-1 * math.log(0.732), node4, node1)
    edge19 = Edge(-1 * math.log(0.650), node4, node2)
    edge20 = Edge(-1 * math.log(1.049), node4, node3)

    # Kết nối đỉnh và cạnh để tạo thành một đồ thị
    node0.adjacency_list.extend([edge1, edge2, edge3, edge4])
    node1.adjacency_list.extend([edge5, edge6, edge7, edge8])
    node2.adjacency_list.extend([edge9, edge10, edge11, edge12])
    node3.adjacency_list.extend([edge13, edge14, edge15, edge16])
    node4.adjacency_list.extend([edge17, edge18, edge19, edge20])

    # Xác định danh sách các đỉnh và cạnh
    vertices = (node0, node1, node2, node3, node4)  # Added missing node0
    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16, edge17, edge18, edge19, edge20)

    # Tạo một thể hiện của thuật toán BellmanFord và tìm đường đi ngắn nhất
    algorithm = BellmanFord(vertices, edges, node1)
    algorithm.calculate_shortest_path()
    algorithm.get_shortest_path_to(node2)
