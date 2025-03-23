# アルゴリズム: 全探索（2重ループによる総当たり）
# 計算量: O(N^2) 

N, Y = map(int, input().split())
xres, yres, zres = -1, -1, -1
for x in range(N + 1):
    for y in range(N + 1):
        # TLE回避のために2重ループに留める
        z = N - x - y
        if z < 0 or z > N:
            continue
        if 10000 * x + 5000 * y + 1000 * z == Y:
            xres, yres, zres = x, y, z
print(xres, yres, zres)