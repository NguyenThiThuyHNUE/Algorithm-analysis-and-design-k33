import sys
from typing import List, Tuple

INF = 10 ** 9

def trace(f: List[List[int]], a: List[List[int]], m: int, n: int) -> List[Tuple[int, int]]:
    # Tìm hàng có giá trị tối đa trong cột cuối cùng
    p = 0
    max_val = -INF
    for i in range(m):
        if f[i][n - 1] > max_val:
            max_val = f[i][n - 1]
            p = i

    tr = []
    q = n - 1
    while q >= 0:
        # Thêm ô (p, q) vào đường đi
        tr.append((p, q))
        # Truy vết theo hướng ngược lại để tìm ô trước đó
        if q > 0:
            if p > 0 and f[p][q] == f[p - 1][q - 1] + a[p][q]:
                p -= 1
            elif p < m - 1 and f[p][q] == f[p + 1][q - 1] + a[p][q]:
                p += 1
            else:
                p = p  # Nếu không khớp, giữ nguyên p (trong trường hợp có đường đi chỉ đi theo hàng hiện tại)
        q -= 1
    return tr[::-1]  # Đảo ngược kết quả vì chúng ta đã truy vết ngược từ cột cuối cùng

def solve(m: int, n: int, a: List[List[int]]) -> None:
    f = [[-INF] * n for _ in range(m)]
    # Khởi tạo giá trị của cột đầu tiên
    for i in range(m):
        f[i][0] = a[i][0]

    for j in range(1, n):
        for i in range(m):
            # Cập nhật giá trị của f[i][j] từ ô (i, j-1), (i-1, j-1), và (i+1, j-1) nếu có
            if i > 0:
                f[i][j] = max(f[i][j], f[i - 1][j - 1] + a[i][j])
            f[i][j] = max(f[i][j], f[i][j - 1] + a[i][j])
            if i < m - 1:
                f[i][j] = max(f[i][j], f[i + 1][j - 1] + a[i][j])

    # Tìm giá trị tối đa trong cột cuối cùng
    res = -INF
    for i in range(m):
        res = max(res, f[i][n - 1])

    print(res)

    tr = trace(f, a, m, n)
    for p, q in tr:
        print(p + 1, q + 1)

def enter() -> Tuple[int, int, List[List[int]]]:
    m, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    return m, n, a

if __name__ == "__main__":
    m, n, a = enter()
    solve(m, n, a)











# import sys
# from typing import List, Tuple

# INF = 10 ** 9

# def trace(f: List[List[int]], a: List[List[int]], m: int, n: int) -> List[Tuple[int, int]]:
#     # First, find the row in column n with the maximum value
#     p, q = 0, n - 1
#     res = -INF  # Ensure that res is defined
#     for i in range(m):
#         if res == f[i][n - 1]:
#             p = i
#             break
#     tr = []
#     while q >= 0:
#         # Add the cell (p, q) to the path
#         tr.append((p, q))
#         if p > 0 and f[p][q] == f[p - 1][q - 1] + a[p][q]:
#             p -= 1
#         elif p < m - 1 and f[p][q] == f[p + 1][q - 1] + a[p][q]:
#             p += 1
#         q -= 1
#     return tr

# def solve(m: int, n: int, a: List[List[int]]) -> None:
#     f = [[-INF] * n for _ in range(m)]
#     for i in range(m):
#         f[i][0] = a[i][0]
#     for j in range(1, n):
#         for i in range(m):
#             if i > 0:
#                 f[i][j] = max(f[i][j], f[i - 1][j - 1] + a[i][j])
#             f[i][j] = max(f[i][j], f[i][j - 1] + a[i][j])
#             if i < m - 1:
#                 f[i][j] = max(f[i][j], f[i + 1][j - 1] + a[i][j])
#     res = -INF
#     for i in range(m):
#         res = max(res, f[i][n - 1])
#     print(res)
#     tr = trace(f, a, m, n)
#     for p, q in tr[::-1]:
#         print(p + 1, q + 1)

# def enter() -> Tuple[int, int, List[List[int]]]:
#     m, n = map(int, input().split())
#     a = [[0] * n for _ in range(m)]
#     for i in range(m):
#         a[i] = list(map(int, input().split()))
#     return m, n, a

# if __name__ == "__main__":
#     m, n, a = enter()
#     solve(m, n, a)
