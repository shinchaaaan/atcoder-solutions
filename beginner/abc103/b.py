# ABC103 B

S = input()
T = input()

ans = "No"
for i in range(len(S)):
    if S == T:
        ans = "Yes"
        break
    else:
        S = S[-1:] + S[:-1] 
print(ans)
    
# k y o t o
# 0 1 2 3 4 