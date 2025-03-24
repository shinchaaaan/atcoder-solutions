def solve():
    N = int(input())

    # 前回の時刻と座標を表す変数
    pt, px, py = 0, 0, 0

    for _ in range(N):
        # 移動先の情報
        t, x, y = map(int, input().split())

        T, X, Y = t - pt, abs(x - px), abs(y - py)

        # 間に合わない時は不可能（時間が足りない）
        if T < X + Y:
            return False
        
        # パリティが合わないときは不可能
        if T % 2 != (X + Y) % 2:
            return False
        
        # 前回情報を更新
        pt, px, py = t, x, y
    
    # 最後まで到達
    return True

print("Yes" if solve() else "No")
