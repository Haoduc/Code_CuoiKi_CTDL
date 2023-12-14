class RadixSort:

    def __init__(self, data):
        # Khởi tạo đối tượng RadixSort với dữ liệu đầu vào
        self.data = data

    def get_digits(self):
        """
        Trả về số chữ số lớn nhất trong dãy số.
        """
        return len(str(max(self.data)))  # Chuyển số lớn nhất trong dãy số thành chuỗi và lấy độ dài của chuỗi
    
    def sort(self):
        """
        Sắp xếp dãy số bằng thuật toán Radix Sort.
        """
        for digit in range(self.get_digits()):  # Duyệt qua từng chữ số
            self.counting_sort(digit)  # Sắp xếp dãy số theo chữ số thứ digit
    
    def counting_sort(self, d):
        """
        Sắp xếp dãy số theo chữ số thứ d bằng thuật toán Counting Sort.
        Dãy số được giả định là ở cơ số 10 (base 10).
        """
        ITEMS_IN_BUCKET = 10  # Giả sử cơ số 10 cho đơn giản

        count_array = [[] for _ in range(ITEMS_IN_BUCKET)]  # Tạo một mảng gồm 10 danh sách rỗng

        for num in self.data:  # Duyệt qua từng số trong dãy số
            index = (num // (10**d)) % 10  # Tính chỉ số của số trong mảng count_array
            count_array[index].append(num)  # Thêm số vào danh sách tương ứng trong mảng count_array
        
        z = 0  # Khởi tạo chỉ số z
        for i in range(len(count_array)):  # Duyệt qua từng danh sách trong mảng count_array
            while len(count_array[i]) > 0:  # Trong khi danh sách vẫn còn phần tử
                self.data[z] = count_array[i].pop(0)  # Lấy phần tử đầu tiên của danh sách và gán vào vị trí z trong dãy số
                z += 1  # Tăng chỉ số z lên 1


if __name__ == '__main__':
    # Ví dụ sử dụng
    n = [1, 18, 10, 1000, 0, 3, 54]  # Danh sách các số cần sắp xếp
    radix_sort = RadixSort(n)  # Khởi tạo đối tượng RadixSort với danh sách cần sắp xếp
    radix_sort.sort()  # Sắp xếp danh sách
    print(radix_sort.data)  # In danh sách đã sắp xếp
