# ABC064 A

digits = input().split()
rgb = int("".join(digits))    
print("YES" if rgb % 4 == 0 else "NO")