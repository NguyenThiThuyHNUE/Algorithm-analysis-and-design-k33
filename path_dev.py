import sys
from typing import List, Tuple

maxN = 105
INF = 10 ** 9

n, m = 0, 0
a: List[List[int]] = [[0 for _ in range(maxN)] for _ in range(maxN)]
f: List[List[int]] = [[-2 * INF for _ in range(maxN)] for _ in range(maxN)]
path: List[List[Tuple[int, int]]] = [[(-1, -1) for _ in range(maxN)] for _ in range(maxN)]

def enter():
    global n, m
    m, n = map(int, input().split())
    for i in range(1, m + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            a[i][j] = row[j - 1]

def dp(i, j):
    if i < 1 or i > m:
        return -INF
    if j == n:
        return a[i][j]
    if f[i][j] != -2 * INF:
        return f[i][j]
    
    # Tính giá trị f[i][j] và cập nhật bảng path
    values = []
    if i > 1:  # Check (i-1, j+1)
        values.append((dp(i - 1, j + 1), (i - 1, j + 1)))
    if j < n:  # Check (i, j+1)
        values.append((dp(i, j + 1), (i, j + 1)))
    if i < m:  # Check (i+1, j+1)
        values.append((dp(i + 1, j + 1), (i + 1, j + 1)))
    
    best_value, best_pos = max(values, key=lambda x: x[0])
    f[i][j] = best_value + a[i][j]
    path[i][j] = best_pos
    
    return f[i][j]

def trace_path(i: int, j: int) -> List[Tuple[int, int]]:
    """Truy vết đường đi từ (i, j) đến cuối"""
    path_trace = []
    while j <= n:
        path_trace.append((i, j))
        i, j = path[i][j]
        if i == -1 or j == -1:  # Đã đến điểm kết thúc
            break
    return path_trace

def main():
    enter()
    
    # Khởi tạo bảng f và path
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            f[i][j] = -2 * INF
            path[i][j] = (-1, -1)
    
    # Tính toán bảng f
    res = -INF
    start_i = 0
    for i in range(1, m + 1):
        if dp(i, 1) > res:
            res = f[i][1]
            start_i = i
    
    print("Giá trị đường đi dài nhất:", res)
    
    # Truy vết và in ra đường đi
    path_trace = trace_path(start_i, 1)
    for p, q in path_trace:
        print(f"({p}, {q})", end=' ')
    print()

if __name__ == "__main__":
    main()