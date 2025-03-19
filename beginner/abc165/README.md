### 問題名

ABC165 - A 問題

### アルゴリズム

単純な while 文

### 別解

```python
K = int(input())
A, B = map(int, input().split())
exist = False
for i in range(A, B + 1):
    if i % K == 0:
        exist = True
        break
print("OK" if exist else "NG")
```

### 参考

- [AtCoder の問題ページ](https://atcoder.jp/contests/abc165/tasks/abc165_a)
