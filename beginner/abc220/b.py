# ABC220 B

K = int(input())
A, B = input().split()

def conv_decimal_number(x):
    x = x[::-1]
    result = 0
    for i, num in enumerate(x):
        result += int(num) * K ** i 
    return result

print(conv_decimal_number(A) * conv_decimal_number(B))    

# K = int(input())
# A, B = map(list,(input().split()))

# sum_a = 0
# sum_b = 0
# for i, a in enumerate(A):
#     sum_a += int(a) * K ** (len(A) - i - 1)  
    
# for i, b in enumerate(B):
#     sum_b += int(b) * K ** (len(B) - i - 1)
    
# print(sum_a * sum_b)