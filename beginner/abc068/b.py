# ABC068 B

N = int(input())
max_count = -1
ans = -1
for i in range(1, N + 1):
    num = i
    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1
    if count > max_count:
        max_count = count
        ans = i
print(ans)