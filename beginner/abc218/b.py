# ABC218 B

P = list(map(int, input().split()))

result = ""
for p in P:
    result += chr(p + 96)

print(result)