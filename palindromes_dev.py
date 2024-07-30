def find_longest_palindrome(s):
    n = len(s)
    max_length = 1  # Khởi tạo độ dài palindrome tối đa
    start_index = 0  # Chỉ số bắt đầu của palindrome dài nhất

    def try_palindrome(first, last):
        nonlocal max_length, start_index
        dd = 0

        if first == last:
            dd = 1
            first -= 1
            last += 1
        else:
            dd = 0

        while first >= 0 and last < n and s[first] == s[last]:
            dd += 2
            first -= 1
            last += 1

        if dd > max_length:
            max_length = dd
            start_index = first + 1

    i = n // 2
    j = n // 2 + 1
    max_length = 1

    while i >= max_length // 2 and j < n - max_length // 2:
        if i >= max_length // 2:
            try_palindrome(i, i)
            try_palindrome(i, i + 1)
        if j < n - max_length // 2:
            try_palindrome(j, j)
            try_palindrome(j, j + 1)
        i -= 1
        j += 1

    return s[start_index:start_index + max_length], start_index, start_index + max_length - 1, max_length

if __name__ == "__main__":
    s = input().strip()
    longest_palindrome, start, end, length = find_longest_palindrome(s)
    print(f"Chuỗi palindrome dài nhất: {longest_palindrome}")
    print(f"Vị trí bắt đầu: {start}")
    print(f"Vị trí kết thúc: {end}")
    print(f"Độ dài: {length}")
