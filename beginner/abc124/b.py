# ABC124 B

n = int(input())
h_list = [int(i) for i in input().split()]

count = 0
high = 0
for i in range(n):
    if high <= h_list[i]:
        high = h_list[i]
        count += 1
print(count)