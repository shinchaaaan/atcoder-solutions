### 問題名

ABC083 - B 問題

### アルゴリズム

整数の各桁を和を計算

### 別解

```python
def calc_sum_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum

N, A, B = map(int, input().split())
total = 0

for i in range(1, N + 1):
    if A <= calc_sum_digits(i) <= B:
        total += i
print(total)
```

### 参考

- [AtCoder の問題ページ](https://atcoder.jp/contests/abc083/tasks/abc083_b)
