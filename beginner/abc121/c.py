# ABC121 C

N, M = map(int, input().split())

shops = [tuple(map(int, input().split())) for _ in range(N)]

shops.sort()

total = 0
cost = 0
for price, amount in shops:
    buy = min(M - total, amount)
    cost += buy * price
    total += buy
    if total == M:
        break
print(cost)
        