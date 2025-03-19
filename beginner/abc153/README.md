### 問題名

ABC153 - A 問題

### アルゴリズム

「//」演算子　と　「%」演算子

### 別解
```python
H, A = map(int, input().split())
count = (H // A if H % A == 0 else H // A + 1)
print(count)
```

### 参考

- [AtCoder の問題ページ](https://atcoder.jp/contests/abc153/tasks/abc153_a)
