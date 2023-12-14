def insertion_sort(nums):
    # Duyệt qua tất cả các phần tử trong danh sách
    for i in range(len(nums)):  # Duyệt từ đầu đến cuối danh sách
        j = i  # Đặt j là i
        # Di chuyển các phần tử của nums[0..i-1] lớn hơn nums[i] về phía trước một vị trí
        while j > 0 and nums[j - 1] > nums[j]:  # Nếu j lớn hơn 0 và phần tử tại vị trí j-1 lớn hơn phần tử tại vị trí j
            # Hoán đổi các phần tử nếu chúng đang ở trong thứ tự sai
            nums[j - 1], nums[j] = nums[j], nums[j - 1]  # Hoán đổi vị trí của hai phần tử
            j = j - 1  # Giảm j đi 1

if __name__ == '__main__':
    # Ví dụ sử dụng
    x = [4, -9, 8, 111, -10, 0, 6, 2, 3]  # Danh sách các số cần sắp xếp
    
    # Gọi hàm insertion_sort để sắp xếp danh sách
    insertion_sort(x)
    
    # In danh sách đã sắp xếp
    print(x)
