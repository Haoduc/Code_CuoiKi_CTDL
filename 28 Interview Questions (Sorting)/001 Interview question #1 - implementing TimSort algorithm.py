import random

class TimSort:

    def __init__(self, data):
        # Nhận dữ liệu đầu vào
        self.data = data

    def sort(self):
        # Bắt đầu sắp xếp
        self.merge_sort(self.data)

    def merge_sort(self, nums):
        # Nếu danh sách chỉ có một phần tử hoặc không có phần tử nào, không cần sắp xếp
        if len(nums) <= 64:
            # Nếu danh sách có ít hơn 64 phần tử, sử dụng sắp xếp chèn
            self.insertion_sort(nums)
            return

        # Chia danh sách thành hai nửa
        middle_index = len(nums) // 2
        left_half = nums[:middle_index]
        right_half = nums[middle_index:]

        # Sắp xếp cả hai nửa
        self.merge_sort(left_half)
        self.merge_sort(right_half)

        # Hợp nhất hai nửa đã sắp xếp
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i = i + 1
            else:
                nums[k] = right_half[j]
                j = j + 1
            k = k + 1

        # Nếu còn phần tử ở nửa trái, thêm chúng vào danh sách
        while i < len(left_half):
            nums[k] = left_half[i]
            i = i + 1
            k = k + 1

        # Nếu còn phần tử ở nửa phải, thêm chúng vào danh sách
        while j < len(right_half):
            nums[k] = right_half[j]
            j = j + 1
            k = k + 1

    def insertion_sort(self, sub_array):
        # Sắp xếp danh sách con bằng thuật toán sắp xếp chèn
        for i in range(len(sub_array)):
            j = i
            while j > 0 and sub_array[j - 1] > sub_array[j]:
                sub_array[j], sub_array[j - 1] = sub_array[j - 1], sub_array[j]
                j = j - 1


if __name__ == "__main__":
    # Tạo danh sách ngẫu nhiên
    n = [n for n in range(100)]
    random.shuffle(n)

    # Sắp xếp danh sách
    sort = TimSort(n)
    sort.sort()

    # In danh sách đã sắp xếp
    print(sort.data)
