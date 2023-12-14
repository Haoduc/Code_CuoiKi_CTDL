from collections import deque

class QuickSortIterative:

    def __init__(self, data):
        self.data = data

    def partition(self, low, high):
        # Chọn pivot ở giữa và hoán đổi vị trí với phần tử ở cuối mảng
        pivot_index = (low + high) // 2
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        # Quét mảng và đưa các phần tử nhỏ hơn hoặc bằng pivot về phía trước
        for j in range(low, high):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low += 1

        # Đặt pivot vào đúng vị trí
        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low

    def sort(self):
        # Sử dụng ngăn xếp để triển khai QuickSort không đệ quy
        stack = deque()

        # Thêm chỉ số bắt đầu và kết thúc của mảng vào ngăn xếp
        stack.append((0, len(self.data) - 1))

        # Khi ngăn xếp không rỗng
        while stack:
            # Lấy chỉ số bắt đầu và kết thúc từ ngăn xếp
            start, end = stack.pop()

            # PHA CHIA - Tạo pivot và đặt pivot vào đúng vị trí
            pivot = self.partition(start, end)

            # PHA CHIẾN nhưng không sử dụng đệ quy - thêm các phần tử mới vào ngăn xếp
            # xem xét mảng con bên trái của pivot
            if pivot - 1 > start:
                stack.append((start, pivot - 1))

            # xem xét mảng con bên phải của pivot
            if pivot + 1 < end:
                stack.append((pivot + 1, end))


if __name__ == '__main__':
    # Mảng đầu vào
    n = [6, 4, 9, 20, 0]

    # Tạo đối tượng QuickSortIterative và thực hiện sắp xếp
    sort = QuickSortIterative(n)
    sort.sort()

    # In mảng đã được sắp xếp
    print(sort.data)
