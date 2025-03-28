# ABC058 B

O = input()
E = input()

result = ""
for i in range(len(E)):
    result += O[i]
    result += E[i]
if len(O) > len(E):
    result += O[-1]
print(result)