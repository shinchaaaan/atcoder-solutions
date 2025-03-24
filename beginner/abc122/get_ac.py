# ABC122 C
# アルゴリズム：累積和

# 文字列の長さ、クエリ数
N, Q = map(int, input().split())

# 文字列
S = input()

# 長さ N+1 の配列を用意（累積和用）
cs = [0] * (N + 1)

for i in range(1, N):
    # S[i-1:i+1] で2文字取り出して「AC」かどうかチェック。
    # "AC" なら True → 1 になる（bool を int に暗黙変換）
    cs[i + 1] = cs[i] + (S[i - 1:i + 1] == "AC")

for _ in range(Q):
    # クエリの入力（1-based index）: 区間 [l, r]
    l, r = map(int, input().split())

    # 0-based index に直すために l を1減らす
    # 例: l=2, r=6 → S[1]〜S[5]
    l -= 1

    # "AC" の出現数 = cs[r]（0〜r-1までのAC数） - cs[l+1]（0〜lまでのAC数）
    print(cs[r] - cs[l + 1])

