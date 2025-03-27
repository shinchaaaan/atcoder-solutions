# ABC115 C

N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()
min_diff = float('inf')
for i in range(N - K + 1):
    diff = h[i + K - 1] - h[i]
    min_diff = min(min_diff, diff)

print(min_diff)