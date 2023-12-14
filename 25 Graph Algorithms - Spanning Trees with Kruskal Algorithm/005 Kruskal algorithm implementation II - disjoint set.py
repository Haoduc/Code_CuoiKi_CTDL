

class Vertex:
    def __init__(self, name):
        self.name = name  # Tên của đỉnh
        self.node = None  # Đỉnh được kết nối với một nút trong Disjoint Set

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight  # Trọng số của cạnh
        self.start_vertex = start_vertex  # Đỉnh bắt đầu của cạnh
        self.target_vertex = target_vertex  # Đỉnh kết thúc của cạnh

    def __lt__(self, other_edge):
        return self.weight < other_edge.weight  # So sánh để sắp xếp các cạnh theo trọng số

class Node:
    def __init__(self, rank, node_id, parent=None):
        self.rank = rank  # Rank của nút trong Disjoint Set
        self.node_id = node_id  # ID của nút trong Disjoint Set
        self.parent = parent  # Nút cha trong Disjoint Set

class DisjointSet:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list  # Danh sách các đỉnh
        self.root_nodes = []  # Danh sách để lưu trữ các nút gốc của các Disjoint Set
        self.make_sets()  # Khởi tạo các Disjoint Set ban đầu

    def find(self, node):
        current_node = node  # Nút hiện tại

        while current_node.parent is not None:  # Nếu nút hiện tại có cha
            current_node = current_node.parent  # Di chuyển đến nút cha
        return current_node  # Trả về nút gốc của tập hợp

    def merge(self, node1, node2):
        root1 = self.find(node1)  # Tìm nút gốc của tập hợp chứa node1
        root2 = self.find(node2)  # Tìm nút gốc của tập hợp chứa node2

        if root1 == root2:  # Nếu cả hai nút đều thuộc cùng một tập hợp
            return  # Không làm gì cả
        if root1.rank < root2.rank:  # Nếu rank của root1 nhỏ hơn rank của root2
            root1.parent = root2  # Đặt root2 làm cha của root1
        elif root1.rank > root2.rank:  # Nếu rank của root1 lớn hơn rank của root2
            root2.parent = root1  # Đặt root1 làm cha của root2
        else:  # Nếu rank của root1 bằng rank của root2
            root2.parent = root1  # Đặt root1 làm cha của root2
            root1.rank = root1.rank + 1  # Tăng rank của root1 lên 1

    def make_sets(self):
        for v in self.vertex_list:  # Duyệt qua tất cả các đỉnh
            node = Node(0, len(self.root_nodes))  # Tạo một nút mới với rank 0 và id là số lượng nút gốc hiện tại
            v.node = node  # Đặt nút mới làm nút của đỉnh
            self.root_nodes.append(node)  # Thêm nút mới vào danh sách nút gốc

class KruskalAlgorithm:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list  # Danh sách các đỉnh
        self.edge_list = edge_list  # Danh sách các cạnh

    def find_mst(self):
        disjoint_set = DisjointSet(self.vertex_list)  # Khởi tạo một Disjoint Set với danh sách đỉnh
        mst = []  # Cây khung nhỏ nhất
        self.edge_list.sort()  # Sắp xếp các cạnh theo trọng số tăng dần
        for edge in self.edge_list:  # Duyệt qua tất cả các cạnh
            u = edge.start_vertex  # Đỉnh bắt đầu của cạnh
            v = edge.target_vertex  # Đỉnh kết thúc của cạnh

            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):  # Nếu u và v không thuộc cùng một tập hợp
                mst.append(edge)  # Thêm cạnh vào cây khung nhỏ nhất
                disjoint_set.merge(u.node, v.node)  # Gộp tập hợp của u và tập hợp của v

        for edge in mst:  # Duyệt qua tất cả các cạnh trong cây khung nhỏ nhất
            print(edge.start_vertex.name, " - ", edge.target_vertex.name, " - ", edge.weight)  # In thông tin cạnh

if __name__ == '__main__':
    # Ví dụ sử dụng
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")
     # khởi tạo các đỉnh khác

    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(6, vertex1, vertex3)
    edge3 = Edge(5, vertex1, vertex5)
    edge4 = Edge(10, vertex1, vertex6)
    edge5 = Edge(3, vertex2, vertex4)
    edge6 = Edge(3, vertex2, vertex5)
    edge7 = Edge(1, vertex3, vertex4)
    edge8 = Edge(2, vertex3, vertex6)
    edge9 = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)
     # khởi tạo các cạnh khác

    vertices = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7]
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11]

    algorithm = KruskalAlgorithm(vertices, edges)
    algorithm.find_mst()
