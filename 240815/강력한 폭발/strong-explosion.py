import sys

n = int(sys.stdin.readline())
l = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
bombs = []
for i in range(n):
    for j in range(n):
        if l[i][j] != 0:
            bombs.append([i, j])
            l[i][j] = 0

max_fired_positoin = [0]

def fire_all_bomb(count):
    count += 1
    if count > len(bombs):
        max_fired_positoin.append(max(max_fired_positoin.pop(), count_fired_positoin()))
        for i in range(n):
            print(l[i])
        print()
        return
    for bomb in bombs:
        fire_first_bomb(bomb[0], bomb[1])
        fire_all_bomb(count)
        recover_first_bomb(bomb[0], bomb[1])
        
        fire_second_bomb(bomb[0], bomb[1])
        fire_all_bomb(count)
        recover_second_bomb(bomb[0], bomb[1])

        fire_third_bomb(bomb[0], bomb[1])
        fire_all_bomb(count)
        recover_third_bomb(bomb[0], bomb[1])
    return

def count_fired_positoin():
    fired_position = 0
    for i in range(n):
        for j in range(n):
            if l[i][j] != 0:
                fired_position += 1
    return fired_position

def fire_first_bomb(x, y):
    fire_position(x-2, y)
    fire_position(x-1, y)
    fire_position(x, y)
    fire_position(x+1, y)
    fire_position(x+2, y)
    return

def fire_second_bomb(x, y):
    fire_position(x-1, y)
    fire_position(x, y-1)
    fire_position(x, y)
    fire_position(x, y+1)
    fire_position(x+1, y)
    return

def fire_third_bomb(x, y):
    fire_position(x-1, y-1)
    fire_position(x-1, y+1)
    fire_position(x, y)
    fire_position(x+1, y-1)
    fire_position(x+1, y+1)
    return


def fire_position(x, y):
    if 0 <= x < n and 0 <= y < n:
        l[x][y] += 1
    return

def recover_first_bomb(x, y):
    recover_position(x-2, y)
    recover_position(x-1, y)
    recover_position(x, y)
    recover_position(x+1, y)
    recover_position(x+2, y)
    return

def recover_second_bomb(x, y):
    recover_position(x-1, y)
    recover_position(x, y-1)
    recover_position(x, y)
    recover_position(x, y+1)
    recover_position(x+1, y)
    return

def recover_third_bomb(x, y):
    recover_position(x-1, y-1)
    recover_position(x-1, y+1)
    recover_position(x, y)
    recover_position(x+1, y-1)
    recover_position(x+1, y+1)
    return

def recover_position(x,y):
    if 0 <= x < n and 0 <= y < n:
        l[x][y] -= 1
    return

fire_all_bomb(0)
print(max_fired_positoin.pop())