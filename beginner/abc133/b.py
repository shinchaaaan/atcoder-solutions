# ABC133 B

N, D = map(int, input().split())
pos = [list(map(int, (input().split()))) for _ in range(N)]

count = 0
for i in range(N - 1):
    for j in range(i+1, N):
        distance = 0
        for k in range(D):
            distance += (pos[i][k] - pos[j][k]) ** 2
        if distance ** 0.5 == int(distance ** 0.5):
            count += 1

print(count)
