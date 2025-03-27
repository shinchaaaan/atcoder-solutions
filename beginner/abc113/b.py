# ABC113 B

N = int(input())
T, A = map(int, input().split())
H = [int(i) for i in input().split()]

ans = 0
ans_list = []
for i in range(N):
    t = abs(T - H[i] * 0.006 - A)
    ans_list.append(t)

ans = ans_list.index(min(ans_list)) + 1
print(ans)
