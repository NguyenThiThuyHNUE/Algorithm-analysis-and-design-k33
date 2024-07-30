if __name__ == '__main__':
    s = ' ' + input().strip()  # Đọc chuỗi đầu vào và loại bỏ khoảng trắng thừa
    n = len(s) - 1  # Chiều dài của chuỗi không tính khoảng trắng thêm vào

    # Khởi tạo bảng phương án
    palin = [[0] * (n + 1) for _ in range(n + 1)]

    # Các chuỗi con có độ dài 1 là palindrome
    for i in range(1, n + 1):
        palin[i][i] = 1

    # Các chuỗi con có độ dài 2
    for i in range(1, n):
        palin[i][i + 1] = 1 if s[i] == s[i + 1] else 0

    # Tính bảng phương án cho các chuỗi con dài hơn
    for length in range(3, n + 1):  # Các chuỗi con dài hơn 2 ký tự
        for i in range(1, n - length + 2):
            j = i + length - 1
            if s[i] == s[j] and palin[i + 1][j - 1]:
                palin[i][j] = 1

    # Tìm chuỗi palindrome dài nhất
    res = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if palin[i][j]:
                res = max(res, j - i + 1)
    
    print(res)