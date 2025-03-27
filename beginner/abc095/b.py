# ABC095 B

n, x = map(int, input().split())
m_list = [int(input()) for _ in range(n)]

count = 0
for m in m_list:
    x -= m
    count += 1

while x >= min(m_list):
    x -= min(m_list)
    count += 1

print(count)