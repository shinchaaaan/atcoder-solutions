# 第3回 PAST E 問題

# アルゴリズム：無向グラフ

# 頂点数、辺数、クエリ数
N, M, Q = map(int, input().split())

# 頂点数 N のグラフ G を定義
G = [[] for _ in range(N)]

# M 本の辺を順に受け取る
for _ in range(M):
    u, v = map(int, input().split())

    # 頂点番号を0始まりにする
    u -= 1
    v -= 1

    # グラフに辺を追加
    G[u].append(v)
    G[v].append(u)

# 初期状態の各頂点の色を入力
col = list(map(int, input().split()))

# 各クエリに答える
for _ in range(Q):
    t, x, *y = map(int, input().split())

    # 頂点番号を0始まりにする
    x -= 1

    print(col[x])

    # タイプ1の場合
    if t == 1:
        # 頂点 x に隣接する各頂点 v の色を更新
        for v in G[x]:
            col[v] = col[x]
    # タイプ2の場合
    else:
        # 頂点 x の色を y に更新
        col[x] = y[0]