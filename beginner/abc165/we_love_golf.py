K = int(input())
A, B = map(int,input().split())
distance = K
is_range = False
while distance <= B:
    if A <= distance <= B:
        is_range = True
        break
    distance += K
print("OK" if is_range else "NG")