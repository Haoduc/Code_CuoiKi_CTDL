class SelectionSortRecursion:

    def __init__(self, nums):
        # Khởi tạo đối tượng với mảng cần sắp xếp
        self.nums = nums

    def find_min(self, a, i, j):
        # Hàm đệ quy để tìm chỉ số của giá trị nhỏ nhất trong mảng a từ chỉ số i đến j
        # i: chỉ số của phần tử đầu tiên cần xem xét (các chỉ số < i đã được sắp xếp)
        # j: chỉ số của phần tử cuối cùng cần xem xét
        if i == j:
            return i

        # Gọi đệ quy với chỉ số tiếp theo (i+1) để tiếp tục tìm kiếm
        next_min_index = self.find_min(a, i + 1, j)

        # So sánh giá trị của phần tử hiện tại (a[i]) với giá trị của phần tử tối thiểu đã tìm được (a[next_min_index])
        # Trả về chỉ số của giá trị nhỏ nhất
        return i if a[i] < a[next_min_index] else next_min_index

    def sort(self):
        # Phương thức công cộng để bắt đầu quá trình sắp xếp
        self.selection_sort(self.nums)

    def selection_sort(self, nums, current_index=0):
        # Hàm đệ quy để thực hiện Selection Sort

        # Nếu đã xem xét tất cả các phần tử, kết thúc đệ quy
        if current_index == len(nums):
            return

        # Tìm chỉ số của phần tử nhỏ nhất từ vị trí hiện tại đến cuối mảng
        min_index = self.find_min(nums, current_index, len(nums) - 1)

        # Nếu chỉ số nhỏ nhất không phải là vị trí hiện tại, hoán đổi chúng
        if min_index != current_index:
            nums[min_index], nums[current_index] = nums[current_index], nums[min_index]

        # Tiếp tục đệ quy với vị trí tiếp theo
        self.selection_sort(nums, current_index + 1)


if __name__ == '__main__':
    # Mảng đầu vào
    n = [16, 5, -99, 0, 1000, 9, 1]
    print(n)

    # Tạo đối tượng SelectionSortRecursion và thực hiện sắp xếp
    sort = SelectionSortRecursion(n)
    sort.sort()

    # In mảng đã được sắp xếp
    print(sort.nums)
