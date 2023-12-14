def shell_sort(nums):
    # Khởi tạo khoảng cách ban đầu
    gap = len(nums) // 2  # Chia độ dài của danh sách cho 2 để lấy khoảng cách ban đầu
    
    # Bắt đầu thuật toán shell sort
    while gap > 0:  # Khi khoảng cách vẫn còn lớn hơn 0
        
        # Duyệt qua từng phần tử của danh sách
        for i in range(gap, len(nums)):  # Duyệt từ phần tử thứ gap đến cuối danh sách
            
            j = i  # Đặt j là i
            
            # Di chuyển phần tử về đúng vị trí trong khoảng cách gap
            while j >= gap and nums[j - gap] < nums[j]:  # Nếu j vẫn còn lớn hơn hoặc bằng gap và phần tử tại vị trí j-gap nhỏ hơn phần tử tại vị trí j
                nums[j], nums[j - gap] = nums[j - gap], nums[j]  # Hoán đổi vị trí của hai phần tử
                j = j - gap  # Giảm j đi gap
        
        # Giảm khoảng cách cho lần lặp tiếp theo
        gap = gap // 2  # Chia khoảng cách cho 2

if __name__ == '__main__':
    # Ví dụ sử dụng
    x = [8, -41, 0, 7, 223, 1, 10, -85]  # Danh sách các số cần sắp xếp
    
    # Gọi hàm shell_sort để sắp xếp danh sách
    shell_sort(x)
    
    # In danh sách đã sắp xếp
    print(x)
