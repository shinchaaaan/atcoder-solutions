# 下、右、上、左、右下、右上、左上、左下
DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]

H, W = map(int, input().split())
S = [input() for i in range(H)]

# 解答用の二次元配列を準備
result = [[0 if v == '.' else '#' for v in row]for row in S]

# 各マス（i, j）を順に処理
for i in range(H):
    for j in range(W):
        # 空きマス以外はそのまま
        if S[i][j] != '.':
            continue
            
        # 周囲８マスの '#' の個数を数える
        for dx, dy in zip(DX, DY):
            ni, nj = i + dx, j + dy

            # マス（ni, nj）が盤面外の場合はスキップ
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            
            # '#'であれば１を増やす    
            if S[ni][nj] == '#':
                result[i][j] += 1

# 出力形式に合わせて出力
for row in result:
    print(*row, sep='')
    