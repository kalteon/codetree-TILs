import sys

n = 4
arr_2d = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
for i in range(n):
    print(sum(arr_2d[i]))