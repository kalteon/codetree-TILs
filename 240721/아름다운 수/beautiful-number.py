import sys

# 1자리 남으면 1
# 2자리 남으면 11, 22
# 3자리 남으면 111, 122, 221, 333,
# 4자리 남으면 1111, 1122, 2211, 2222, 1333, 3331 4444
n = int(sys.stdin.readline())
number_len = 0
count = 0
def count_beautiful_n_digit_number(current_len, count):
    if current_len == n: 
        return 1
    elif current_len > n:
        return 0
    else:
        for i in range(1, 5):
            current_len += i
            count += count_beautiful_n_digit_number(current_len, count)
            current_len -= i
        return count

print(count_beautiful_n_digit_number(number_len, count))