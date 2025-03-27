# ABC132 C

from statistics import median

N = int(input())
d = list(map(int, input().split()))

d.sort()

ans = d[N // 2] - d[N // 2 - 1]
print(ans)