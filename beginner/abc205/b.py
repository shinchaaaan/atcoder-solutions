# ABC205 B

N = int(input())
A = [int(i) for i in input().split()]
a = [int(i) for i in range(1, N + 1)]

A.sort()

print("Yes" if A == a else "No")