import sys

n = int(sys.stdin.readline())
l = []
check_count = []
n = 2
def count_beautiful_n_digit_number():
    if len(l) == n:
        print()
        check_count.append(1)
        return
    elif len(l) > n:
        return
    else:
        for i in range(1, 5):
            for j in range(i):
                l.append(i)
            count_beautiful_n_digit_number()
            for j in range(i):
                l.pop()
        return

count_beautiful_n_digit_number()
print(sum(check_count))