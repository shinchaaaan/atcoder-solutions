# ABC206 B

N = int(input())

total, i = 0, 1
while total < N:
    total += i
    i += 1
print(i - 1)
