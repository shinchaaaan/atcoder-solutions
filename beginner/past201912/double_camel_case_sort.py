# 第1回 PAST F 問題
# アルゴリズム：連長圧縮

S = (input())
words = []
i = 0
while i < len(S):
    j = i + 1
    while j < len(S) and S[j].islower():
        j += 1

    words.append(S[i:j + 1]) 
    i = j + 1

words.sort(key=str.lower)
print("".join(words))