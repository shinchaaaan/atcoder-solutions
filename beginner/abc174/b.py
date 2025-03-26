# ABC174 B
from math import sqrt
N, D = map(int, input().split())

count = 0
for _ in range(N):
    x, y = map(int, input().split())
    if D >= sqrt(x ** 2 + y ** 2):
        count += 1
print(count)