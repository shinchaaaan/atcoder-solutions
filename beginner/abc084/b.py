# ABC084 B
import re

A, B = map(int, input().split())
S = input()

pattern = rf"^\d{{{A}}}-\d{{{B}}}$"

if re.fullmatch(pattern, S):
    print("Yes")
else:
    print("No")

# ans = "Yes"
# for i in range(A + 1 + B):
#     if i == A:
#         if S[i] != '-':
#             ans = "No"
#             break        
#     elif not S[i].isdigit():
#         ans = "No"
#         break


# print(ans)