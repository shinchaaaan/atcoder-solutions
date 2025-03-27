# ABC130 B

n, x = map(int, input().split())
l = [int(i) for i in input().split()]

d = [0]
for i in range(1, n + 1):

    d.append(d[i-1] + l[i-1]) 

ans = len([i for i in d if i <= x])
print(ans)
    