# ABC164 B

A, B, C, D = map(int, input().split())

i = 0
while True:
    C -= B
    if C <= 0:
        print("Yes")
        break
    A -= D
    if A <= 0:
        print("No")
        break
