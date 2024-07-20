import sys

k, n = map(int, sys.stdin.readline().split())
l = []

def print_k_tree_n_len():
    if len(l) == n:
        for v in l:
            print(v, end = " ")
        print()
        return
    for v in range(1, k + 1):
        l.append(v)
        print_k_tree_n_len()
        l.pop()

print_k_tree_n_len()