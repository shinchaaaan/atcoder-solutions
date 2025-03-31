# ABC066 B

S = input()

while len(S) > 1:
    S = S[:-1]
    if len(S) % 2 == 0:
        half = len(S) // 2
        if S[:half] == S[half:]:
            print(len(S))
            break

