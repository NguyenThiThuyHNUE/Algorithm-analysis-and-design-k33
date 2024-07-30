if __name__ == '__main__':
    s = ' ' + input().strip()  # Đọc chuỗi đầu vào và loại bỏ khoảng trắng thừa
    n = len(s) - 1  # Chiều dài của chuỗi không tính khoảng trắng thêm vào

    # Khởi tạo bảng phương án
    palin = [[0] * (n + 1) for _ in range(n + 1)]
    start = [[0] * (n + 1) for _ in range(n + 1)]  # Bảng lưu chỉ số bắt đầu
    end = [[0] * (n + 1) for _ in range(n + 1)]  # Bảng lưu chỉ số kết thúc

    # Các chuỗi con có độ dài 1 là palindrome
    for i in range(1, n + 1):
        palin[i][i] = 1
        start[i][i] = i
        end[i][i] = i

    # Các chuỗi con có độ dài 2
    for i in range(1, n):
        if s[i] == s[i + 1]:
            palin[i][i + 1] = 1
            start[i][i + 1] = i
            end[i][i + 1] = i + 1

    # Tính bảng phương án cho các chuỗi con dài hơn
    for length in range(3, n + 1):  # Các chuỗi con dài hơn 2 ký tự
        for i in range(1, n - length + 2):
            j = i + length - 1
            if s[i] == s[j] and palin[i + 1][j - 1]:
                palin[i][j] = 1
                start[i][j] = i
                end[i][j] = j

    # Tìm chuỗi palindrome dài nhất
    max_length = 0
    start_index = 0
    end_index = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if palin[i][j]:
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    start_index = start[i][j]
                    end_index = end[i][j]

    # In kết quả
    if max_length > 0:
        print(f"Chuỗi palindrome dài nhất: {s[start_index:end_index + 1]}")
        print(f"Vị trí bắt đầu: {start_index}")
        print(f"Vị trí kết thúc: {end_index}")
        print(f"Độ dài: {max_length}")
    else:
        print("Không có chuỗi palindrome.")
