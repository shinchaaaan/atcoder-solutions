# ABC105 B

N = int(input())

ans = "No"
for i in range(100):
    for j in range(100):
        if i * 4 + j * 7 == N:
            ans = "Yes"
            break
    if ans == "Yes":
        break
print(ans)