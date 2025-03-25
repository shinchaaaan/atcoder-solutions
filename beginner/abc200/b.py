# ABC200 B

N, K = map(int, input().split())

num = 0
for _ in range(K):
    if N % 200 == 0:
        N = N // 200
    else:
        N = int(str(N) + "200")
print(N)