import sys
from typing import List

maxN = 105
INF = 10 ** 9

n, m = 0, 0
a: List[List[int]] = [[0 for _ in range(maxN)] for _ in range(maxN)]
f: List[List[int]] = [[0 for _ in range(maxN)] for _ in range(maxN)]

def enter():
    global n, m
    m, n = map(int, input("Nhap so: ").split())
    for i in range(1, m + 1):
        a[i][1:n+1] = list(map(int, input().split()))

def solve():
    for i in range(0, m + 1):
        f[i][0] = 0
    for i in range(0, n + 1):
        f[0][i] = -INF
    for i in range(0, n + 1):
        f[m+1][i] = -INF
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            f[i][j] = max(max(f[i-1][j-1], f[i][j-1]), f[i+1][j-1]) + a[i][j]
    res = -INF
    for i in range(1, m + 1):
        res = max(res, f[i][n])
    print(res)

if __name__ == "__main__":
    enter()
    solve()