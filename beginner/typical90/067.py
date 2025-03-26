# 競プロ典型90問 067

def base_10_to(n, b):
    if n // b:
        return base_10_to(n // b, b) + str(n % b)
    return str(n % b)

N, K = map(int, input().split())

num = str(N)

for i in range(K):
    base_10 = int(num, 8)
    base_9 = str(base_10_to(base_10, 9))
    num = ""
    for j in range(len(base_9)):
        if base_9[j] == "8":
            num += "5"
        else:
            num += base_9[j]
            
print(num)