import heapq  # Thư viện hỗ trợ các hàm heap

class Vertex:

    def __init__(self, name):
        self.name = name  # Tên của đỉnh
        self.adjacency_list = []  # Danh sách các cạnh kề của đỉnh

class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight  # Trọng số của cạnh
        self.start_vertex = start_vertex  # Đỉnh bắt đầu của cạnh
        self.target_vertex = target_vertex  # Đỉnh kết thúc của cạnh

    def __lt__(self, other_edge):
        return self.weight < other_edge.weight  # So sánh để sắp xếp các cạnh theo trọng số

class PrimsJarnikAlgorithm:

    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list  # Danh sách các đỉnh chưa được thăm
        self.mst = []  # Cây khung nhỏ nhất
        self.total_cost = 0  # Tổng trọng số của cây khung nhỏ nhất
        self.heap = []  # Heap để lưu trữ các cạnh có thể chọn

    def find_spanning_tree(self, start_vertex):
        self.unvisited_list.remove(start_vertex)  # Loại bỏ đỉnh bắt đầu khỏi danh sách các đỉnh chưa được thăm
        actual_vertex = start_vertex  # Đặt đỉnh bắt đầu làm đỉnh hiện tại
        
        while self.unvisited_list:  # Khi còn đỉnh chưa được thăm
            for edge in actual_vertex.adjacency_list:  # Duyệt qua tất cả các cạnh kề với đỉnh hiện tại
                if edge.target_vertex in self.unvisited_list:  # Nếu đỉnh kết thúc của cạnh chưa được thăm
                    heapq.heappush(self.heap, edge)  # Thêm cạnh vào heap

            min_edge = heapq.heappop(self.heap)  # Lấy ra cạnh có trọng số nhỏ nhất từ heap

            if min_edge.target_vertex in self.unvisited_list:  # Nếu đỉnh kết thúc của cạnh chưa được thăm
                self.mst.append(min_edge)  # Thêm cạnh vào cây khung nhỏ nhất
                print("Edge added to spanning tree: %s - %s" % (min_edge.start_vertex.name, min_edge.target_vertex.name))  # In thông tin cạnh đã thêm
                self.total_cost += min_edge.weight  # Cập nhật tổng trọng số
                actual_vertex = min_edge.target_vertex  # Đặt đỉnh kết thúc của cạnh làm đỉnh hiện tại
                self.unvisited_list.remove(actual_vertex)  # Loại bỏ đỉnh hiện tại khỏi danh sách các đỉnh chưa được thăm

    def get_mst(self):
        return self.mst  # Trả về cây khung nhỏ nhất

    def get_total_cost(self):
        return self.total_cost  # Trả về tổng trọng số

if __name__ == '__main__':
    # Ví dụ sử dụng
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")
    # khởi tạo các đỉnh khác

    edgeAB = Edge(2, vertexA, vertexB)
    edgeBA = Edge(2, vertexB, vertexA)
    edgeAE = Edge(5, vertexA, vertexE)
    edgeEA = Edge(5, vertexE, vertexA)
    edgeAC = Edge(6, vertexA, vertexC)
    edgeCA = Edge(6, vertexC, vertexA)
    edgeAF = Edge(10, vertexA, vertexF)
    edgeFA = Edge(10, vertexF, vertexA)
    edgeBE = Edge(3, vertexB, vertexE)
    edgeEB = Edge(3, vertexE, vertexB)
    edgeBD = Edge(3, vertexB, vertexD)
    edgeDB = Edge(3, vertexD, vertexB)
    edgeCD = Edge(1, vertexC, vertexD)
    edgeDC = Edge(1, vertexD, vertexC)
    edgeCF = Edge(2, vertexC, vertexF)
    edgeFC = Edge(2, vertexF, vertexC)
    edgeDE = Edge(4, vertexD, vertexE)
    edgeED = Edge(4, vertexE, vertexD)
    edgeDG = Edge(5, vertexD, vertexG)
    edgeGD = Edge(5, vertexG, vertexD)
    edgeFG = Edge(5, vertexF, vertexG)
    edgeGF = Edge(5, vertexG, vertexF)
    # khởi tạo các cạnh khác

    unvisited_list = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG]

    
    # Gán danh sách cạnh kề cho mỗi đỉnh
    vertexA.adjacency_list.append(edgeAB)
    vertexA.adjacency_list.append(edgeAC)
    vertexA.adjacency_list.append(edgeAE)
    vertexA.adjacency_list.append(edgeAF)
    vertexB.adjacency_list.append(edgeBA)
    vertexB.adjacency_list.append(edgeBD)
    vertexB.adjacency_list.append(edgeBE)
    vertexC.adjacency_list.append(edgeCA)
    vertexC.adjacency_list.append(edgeCD)
    vertexC.adjacency_list.append(edgeCF)
    vertexD.adjacency_list.append(edgeDB)
    vertexD.adjacency_list.append(edgeDC)
    vertexD.adjacency_list.append(edgeDE)
    vertexD.adjacency_list.append(edgeDG)
    vertexE.adjacency_list.append(edgeEA)
    vertexE.adjacency_list.append(edgeEB)
    vertexE.adjacency_list.append(edgeED)
    vertexF.adjacency_list.append(edgeFA)
    vertexF.adjacency_list.append(edgeFC)
    vertexF.adjacency_list.append(edgeFG)
    vertexG.adjacency_list.append(edgeGD)
    vertexG.adjacency_list.append(edgeGF)

    algorithm = PrimsJarnikAlgorithm(unvisited_list)
    algorithm.find_spanning_tree(vertexD)
    print(algorithm.get_total_cost())  # In tổng trọng số của cây khung nhỏ nhất
