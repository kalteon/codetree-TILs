import sys

sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
l = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
boom_positoin = []
sum_list = []
def maximumize_explosion_position():
    if not boom_positoin:
        sum_v = 0
        for i in range(n):
            for j in l[i]:
                if l[i][j] > 0:
                    sum_v += 1
        sum_list.append(sum_v)
        return
    else:
        current_position = boom_positoin.pop()
        x, y = current_position[0], current_position[1]
        do_first(x, y, 1)
        maximumize_explosion_position()
        do_first(x, y, -1)
        boom_positoin.append(current_position)

        current_position = boom_positoin.pop()
        x, y = current_position[0], current_position[1]
        do_second(x, y, 1)
        maximumize_explosion_position()
        do_second(x, y, -1)
        boom_positoin.append(current_position)

        current_position = boom_positoin.pop()
        x, y = current_position[0], current_position[1]
        do_third(x, y, 1)
        maximumize_explosion_position()
        do_third(x, y, -1)
        boom_positoin.append(current_position)
    return

def do_first(x, y, v):
    l[x][max(0, y-2)] += v
    l[x][max(0, y-1)] += v
    l[x][y] += v
    l[x][min(n-1, y+1)] += v
    l[x][min(n-1, y+2)] += v

def do_second(x, y, v):
    l[max(0, x-1)][y] += v
    l[x][max(0, y-1)] += v
    l[x][y] += v
    l[min(n-1, x+1)][y] += v
    l[x][min(n-1, y+1)] += v

def do_third(x, y, v):
    l[x][y] += v
    if x > 0 and y > 0:
        l[x-1][y-1] += v
    if x > 0 and y < n-1:
        l[x-1][y+1] += v
    if x < n-1 and y > 0:
        l[x+1][y-1] += v
    if x < n-1 and y < n-1:
        l[x+1][y+1] += v

for i in range(n):
        for j in range(n):
            if l[i][j] == 1:
                boom_positoin.append([i, j])
                l[i][j] = 0

maximumize_explosion_position()
print(max(sum_list))