# ABC214 B

S, T = map(int, input().split())

count = 0
for a in range(S + 1):
    for b in range(S + 1 - a):
        for c in range(S + 1 - a - b):
            if a * b * c <= T:
                count += 1
print(count)