import sys


def find_max_area(index):
    global max_bombed_area

    if index == len(bomb_pos):
        max_bombed_area = max(max_bombed_area, cal_area())
        return
    
    for i in range(1, 4):
        x, y = bomb_pos[index]

        bomb_type[x][y] = i
        find_max_area(index + 1)
        bomb_type[x][y] = 0
    
def cal_area():
    for i in range(n):
        for j in range(n):
            bombed_area[i][j] = False
    
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])
    
    area = 0
    for i in range(n):
        for j in range(n):
            if bombed_area[i][j]:
                area += 1
    
    return area

def bomb(x, y, b_type):
    bomb_shapes = [
        [],
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]
    
    # 격자 내 칸에 대해서만 영역을 표시합니다.
    for i in range(5):
        dx, dy = bomb_shapes[b_type][i];
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            bombed_area[nx][ny] = True

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(sys.stdin.readline())
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]
bombed_area = [
    [False for _ in range(n)]
    for _ in range(n)
]

max_bombed_area = 0

bomb_pos = []

for i in range(n):
    given_row = list(map(int, input().split()))
    for j, bomb_place in enumerate(given_row):
        if bomb_place:
            bomb_pos.append((i, j))

find_max_area(0)

print(max_bombed_area)