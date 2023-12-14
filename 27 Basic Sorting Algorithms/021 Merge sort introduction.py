def merge_sort(nums):
    # Nếu danh sách chỉ có một phần tử hoặc là danh sách rỗng, không cần sắp xếp
    if len(nums) == 1:
        return
    
    # Chia danh sách thành hai nửa
    middle_index = len(nums) // 2  # Tính chỉ số giữa
    left_half = nums[:middle_index]  # Lấy nửa trái của danh sách
    right_half = nums[middle_index:]  # Lấy nửa phải của danh sách

    # Gọi đệ quy sắp xếp cho cả hai nửa
    merge_sort(left_half)  # Sắp xếp nửa trái
    merge_sort(right_half)  # Sắp xếp nửa phải

    # Khởi tạo các biến chỉ mục cho danh sách đã sắp xếp
    i = 0  # Chỉ số cho nửa trái
    j = 0  # Chỉ số cho nửa phải
    k = 0  # Chỉ số cho danh sách gốc

    # Hợp nhất các nửa đã sắp xếp vào danh sách gốc
    while i < len(left_half) and j < len(right_half):  # Trong khi cả hai nửa đều còn phần tử
        if left_half[i] < right_half[j]:  # Nếu phần tử của nửa trái nhỏ hơn phần tử của nửa phải
            nums[k] = left_half[i]  # Đưa phần tử của nửa trái vào danh sách gốc
            i += 1  # Tăng chỉ số của nửa trái
        else:
            nums[k] = right_half[j]  # Ngược lại, đưa phần tử của nửa phải vào danh sách gốc
            j += 1  # Tăng chỉ số của nửa phải
        k += 1  # Tăng chỉ số của danh sách gốc
    
    # Sao chép các phần tử còn lại của nửa trái (nếu có)
    while i < len(left_half):  # Trong khi nửa trái vẫn còn phần tử
        nums[k] = left_half[i]  # Đưa phần tử của nửa trái vào danh sách gốc
        i += 1  # Tăng chỉ số của nửa trái
        k += 1  # Tăng chỉ số của danh sách gốc

    # Sao chép các phần tử còn lại của nửa phải (nếu có)
    while j < len(right_half):  # Trong khi nửa phải vẫn còn phần tử
        nums[k] = right_half[j]  # Đưa phần tử của nửa phải vào danh sách gốc
        j += 1  # Tăng chỉ số của nửa phải
        k += 1  # Tăng chỉ số của danh sách gốc

if __name__ == '__main__':
    # Khởi tạo danh sách cần sắp xếp
    my_list = [1, 3, 4, -1, 99, -6, 0]

    # Gọi hàm sắp xếp và in kết quả
    merge_sort(my_list)
    print(my_list)
