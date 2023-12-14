class BubbleSort:
    
    def __init__(self, nums):
        # Hàm khởi tạo để khởi tạo đối tượng BubbleSort với một danh sách số nguyên
        self.nums = nums
        
    def sort(self):
        # Thuật toán sắp xếp Bubble Sort
        for i in range(len(self.nums)-1):  # Duyệt qua tất cả các phần tử trong danh sách
            for j in range(len(self.nums)-i-1):  # Duyệt qua các phần tử chưa được sắp xếp
                # So sánh các phần tử kề nhau và hoán đổi nếu chúng ở trong thứ tự sai
                if self.nums[j] > self.nums[j+1]:  # Nếu phần tử hiện tại lớn hơn phần tử tiếp theo
                    self.swap(j, j+1)  # Hoán đổi vị trí của hai phần tử
    
    def swap(self, i, j):
        # Hàm trợ giúp để hoán đổi các phần tử tại các chỉ số i và j
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]  # Hoán đổi vị trí của hai phần tử

if __name__ == '__main__':
    # Ví dụ sử dụng
    n = [1, -5, 0, 2, -1, 10, 9, 100, 56, -34]  # Danh sách các số cần sắp xếp
    
    # Tạo đối tượng BubbleSort với danh sách số nguyên
    bubble_sort = BubbleSort(n)
    
    # Sắp xếp danh sách bằng thuật toán BubbleSort
    bubble_sort.sort()
    
    # In danh sách đã sắp xếp
    print("Danh sách đã sắp xếp:", bubble_sort.nums)
