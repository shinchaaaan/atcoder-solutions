# ABC144 B

N = int(input())

ans = "No"
for i in range(1, 10):
    for j in range(1,10):
        if i * j == N:
            ans = "Yes"
            break
    if ans == "Yes":
        break
    
print(ans)