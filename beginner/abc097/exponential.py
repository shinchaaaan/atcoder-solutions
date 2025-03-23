# 全探索

X = int(input())
max_value = 1
# (2, int(X ** 0.5 + 1))にすると計算量削減 X ** 0.5 === √X
for b in range(2, X + 1):
    p = 2
    while True:
        value = b ** p
        if value > X:
            break
        if value > max_value:
            max_value = value
        p += 1
print(max_value)