N, A, B = map(int, input().split())
total = 0
for i in range(1, N + 1):
    digit_sum = 0
    digits = [int(d) for d in str(i)]
    for digit in digits:
        digit_sum += digit
    if A <= digit_sum <= B:
        total += i
print(total)