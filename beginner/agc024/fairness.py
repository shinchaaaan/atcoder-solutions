# AGC024 A
# アルゴリズム：周期性

A, B, C, K = map(int, input().split())

print(A - B if K % 2 == 0 else B - A)