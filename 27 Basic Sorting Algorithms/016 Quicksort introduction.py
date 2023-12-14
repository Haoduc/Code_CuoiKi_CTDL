class QuickSort:

    def __init__(self, data):
        # Nhận dữ liệu đầu vào để sắp xếp
        self.data = data

    def sort(self):
        # Bắt đầu quá trình sắp xếp
        self.quick_sort(0, len(self.data)-1)

    def quick_sort(self, low, high):
        # Nếu chỉ có một phần tử hoặc không có phần tử nào, không cần làm gì cả
        if low >= high:
            return
        
        # Chia dữ liệu thành hai phần, một phần nhỏ hơn và một phần lớn hơn so với phần tử chốt (pivot)
        pivot_index = self.partition(low, high)
        
        # Sắp xếp hai phần này một cách đệ quy
        self.quick_sort(low, pivot_index-1)
        self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        # Chọn phần tử chốt ở giữa dữ liệu
        pivot_index = (low + high) // 2
        
        # Đưa phần tử chốt về cuối dữ liệu
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        # Duyệt qua từng phần tử của dữ liệu
        for j in range(low, high):
            # Nếu phần tử nhỏ hơn hoặc bằng phần tử chốt
            if self.data[j] <= self.data[high]:
                # Đưa phần tử này về phía trước dữ liệu
                self.data[low], self.data[j] = self.data[j], self.data[low]
                # Tăng chỉ số low lên 1
                low = low + 1 

        # Đưa phần tử chốt về đúng vị trí của nó trong dữ liệu đã sắp xếp
        self.data[low], self.data[high] = self.data[high], self.data[low]

        # Trả về vị trí của phần tử chốt
        return low

if __name__ == '__main__':
    # Ví dụ sử dụng
    x = [1, -6, 0, 190, 5, 8, 9, 99]

    algorithm = QuickSort(x)
    algorithm.sort()
    print(x)
