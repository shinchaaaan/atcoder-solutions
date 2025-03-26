# ABC090 B

A, B = map(int, input().split())

count = 0
for i in range(A, B + 1):
    str_num = str(i)
    if str_num == str_num[::-1]:
        count += 1
print(count)