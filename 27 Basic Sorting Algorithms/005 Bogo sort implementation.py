import random  # Thư viện hỗ trợ các hàm ngẫu nhiên

class BogoSort:
    def __init__(self, nums):
        self.nums = nums  # Danh sách các số cần sắp xếp
    
    def sort(self):
        # Tiếp tục trộn đến khi dãy đã được sắp xếp
        while not self.is_sorted():  # Nếu danh sách chưa được sắp xếp
            print('Shuffle again...')  # Thông báo cho người dùng biết rằng một lần trộn khác đang được thực hiện
            self.shuffle()  # Trộn danh sách
        print('Sorted result:', self.nums)  # In ra kết quả đã được sắp xếp
    
    def shuffle(self):
        # Duyệt qua danh sách và đổi chỗ các phần tử một cách ngẫu nhiên
        for i in range(len(self.nums)-2, 0, -1):  # Duyệt từ cuối danh sách đến đầu danh sách
            j = random.randint(0, i)  # Chọn một vị trí ngẫu nhiên từ 0 đến i
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]  # Đổi chỗ phần tử tại vị trí i và vị trí j
        
    def is_sorted(self):
        # Kiểm tra xem danh sách đã được sắp xếp hay chưa
        return all(self.nums[i] <= self.nums[i + 1] for i in range(len(self.nums) - 1))  # Kiểm tra xem mỗi cặp phần tử liên tiếp có được sắp xếp tăng dần hay không

if __name__ == '__main__':
    # Ví dụ sử dụng
    nums_to_sort = [1, -4, 0, 10, 12, -5, 1, 2, -1, 34]  # Danh sách các số cần sắp xếp
    algorithm = BogoSort(nums_to_sort)  # Khởi tạo thuật toán BogoSort với danh sách cần sắp xếp
    algorithm.sort()  # Sắp xếp danh sách
