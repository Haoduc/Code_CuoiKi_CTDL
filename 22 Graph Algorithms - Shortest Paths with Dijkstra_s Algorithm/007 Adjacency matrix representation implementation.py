import sys  # Thư viện hỗ trợ các hàm hệ thống

class DijkstraAlgorithm:

    def __init__(self, adjacency_matrix, start_vertex):
        # Khởi tạo DijkstraAlgorithm với ma trận kề và đỉnh bắt đầu
        self.adjacency_matrix = adjacency_matrix  # Ma trận kề biểu diễn đồ thị
        self.start_vertex = start_vertex  # Đỉnh bắt đầu
        self.v = len(adjacency_matrix)  # Số lượng đỉnh trong đồ thị
        self.visited = [False for _ in range(len(adjacency_matrix))]  # Danh sách kiểm tra xem đỉnh đã được thăm chưa
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]  # Danh sách khoảng cách từ đỉnh bắt đầu đến mỗi đỉnh
        self.distances[start_vertex] = 0  # Khoảng cách từ đỉnh bắt đầu đến chính nó là 0

    def get_min_vertex(self):
        # Tìm đỉnh có giá trị khoảng cách nhỏ nhất trong số các đỉnh chưa thăm
        min_vertex_value = sys.maxsize  # Giá trị khoảng cách nhỏ nhất, khởi tạo là giá trị lớn nhất có thể
        min_vertex_index = 0  # Đỉnh có giá trị khoảng cách nhỏ nhất

        for index in range(self.v):  # Duyệt qua tất cả các đỉnh
            if not self.visited[index] and self.distances[index] < min_vertex_value:  # Nếu đỉnh chưa được thăm và có khoảng cách nhỏ hơn giá trị nhỏ nhất hiện tại
                min_vertex_value = self.distances[index]  # Cập nhật giá trị nhỏ nhất
                min_vertex_index = index  # Cập nhật đỉnh có giá trị nhỏ nhất

        return min_vertex_index  # Trả về đỉnh có giá trị nhỏ nhất

    def calculate(self):
        # Tính toán các khoảng cách ngắn nhất đến tất cả các đỉnh sử dụng thuật toán Dijkstra
        for vertex in range(self.v):  # Duyệt qua tất cả các đỉnh
            actual_vertex = self.get_min_vertex()  # Lấy đỉnh có giá trị nhỏ nhất
            print('Xét đỉnh %s' % actual_vertex)  # In thông báo xét đỉnh
            self.visited[actual_vertex] = True  # Đánh dấu đỉnh đã được xét

            for other_vertex in range(self.v):  # Duyệt qua tất cả các đỉnh khác
                if self.adjacency_matrix[actual_vertex][other_vertex] > 0:  # Nếu có cạnh nối giữa hai đỉnh
                    # Bước thư giãn: Cập nhật khoảng cách nếu tìm thấy một đường đi ngắn hơn
                    if self.distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex] < self.distances[other_vertex]:
                        self.distances[other_vertex] = self.distances[actual_vertex] + \
                            self.adjacency_matrix[actual_vertex][other_vertex]  # Cập nhật khoảng cách mới

    def print_distance(self):
        # In các khoảng cách tính toán từ đỉnh bắt đầu đến tất cả các đỉnh khác
        print(self.distances)  # In danh sách khoảng cách

if __name__ == '__main__':
    # Ma trận kề mẫu đại diện cho một đồ thị
    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 0],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]
    
    # Tạo một thể hiện của DijkstraAlgorithm và chạy thuật toán
    algorithm = DijkstraAlgorithm(m, 1)  # Khởi tạo thuật toán với ma trận kề và đỉnh bắt đầu
    algorithm.calculate()  # Chạy thuật toán để tính toán khoảng cách
    
    # In các khoảng cách tính toán
    algorithm.print_distance()  # In danh sách khoảng cách
