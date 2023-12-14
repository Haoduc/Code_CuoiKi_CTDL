def selection_sort(nums):
    # Duyệt qua tất cả các phần tử trong mảng
    for i in range(len(nums)-1):  # Duyệt từ đầu đến cuối mảng
        index = i  # Đặt chỉ số của phần tử nhỏ nhất là i
        
        # Tìm phần tử nhỏ nhất trong phần còn lại của mảng chưa được sắp xếp
        for j in range(i, len(nums)):  # Duyệt từ i đến cuối mảng
            if nums[j] < nums[index]:  # Nếu phần tử tại vị trí j nhỏ hơn phần tử tại vị trí index
                index = j  # Cập nhật index
        
        # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên
        if index != i:  # Nếu index khác i
            nums[index], nums[i] = nums[i], nums[index]  # Hoán đổi phần tử tại vị trí index và i

if __name__ == '__main__':
    # Ví dụ sử dụng
    n = [10, 2, 4, 0, 1]  # Danh sách các số cần sắp xếp
    
    # Gọi hàm selection_sort để sắp xếp danh sách
    selection_sort(n)
    
    # In danh sách đã sắp xếp
    print(n)
