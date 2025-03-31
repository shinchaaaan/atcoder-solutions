# ABC157 B

bingo = [list(map(int, input().split())) for _ in range(3)]
N = int(input())

punched = [[False] * 3 for _ in range(3)]
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == bingo[i][j]:
                punched[i][j] = True

ans = False
for row in punched:
    if all(row):
        ans = True

for col in range(3):
    if all(punched[row][col] for row in range(3)):
        ans = True

if all(punched[i][i] for i in range(3)) or all(punched[i][2 - i] for i in range(3)):
    ans = True

print("Yes" if ans else "No")

