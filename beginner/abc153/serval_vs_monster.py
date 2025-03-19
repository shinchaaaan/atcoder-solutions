H, A = map(int,input().split())
count = 1
while (H := H - A) > 0:
    count += 1
print(count) 