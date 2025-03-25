# ABC158 C

A, B = map(int, input().split())

result = -1
for i in range(1, 10000):
    a = i * 8 // 100
    b = i * 10 // 100
    if a == A and b == B:
        result = i
        break
print(result)