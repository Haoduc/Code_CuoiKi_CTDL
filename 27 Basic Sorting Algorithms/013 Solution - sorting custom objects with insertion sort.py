class Person:
    def __init__(self, name, age):
        # Hàm khởi tạo với hai tham số: tên và tuổi
        self.name = name
        self.age = age

    def __lt__(self, other):
        # Hàm so sánh nhỏ hơn, được sử dụng khi Python cần so sánh hai đối tượng Person
        # Trong trường hợp này, một người được coi là "nhỏ hơn" nếu tuổi của họ nhỏ hơn tuổi của người khác
        return self.age < other.age

    def __repr__(self):
        # Hàm biểu diễn chuỗi, được gọi khi Python cần chuyển đổi một đối tượng Person thành chuỗi
        # Trong trường hợp này, chúng ta chỉ cần trả về tên của người
        return str(self.name)

def insertion_sort(people):
    # Thuật toán sắp xếp chèn
    for i in range(len(people)):
        j = i
        # Di chuyển các phần tử của people[0..i-1], lớn hơn people[i],
        # về phía trước một vị trí trước khi chèn people[i] vào đúng vị trí
        while j > 0 and people[j - 1] > people[j]:
            people[j], people[j - 1] = people[j - 1], people[j]
            j = j - 1

if __name__ == '__main__':
    # Ví dụ sử dụng
    n = [Person('Adam', 23), Person('Ana', 17), Person('Kevin', 32), Person('Daniel', 37)]
    # Gọi hàm insertion_sort để sắp xếp danh sách
    insertion_sort(n)
    # In danh sách đã sắp xếp
    print(n)
