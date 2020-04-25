s, n = map(int, input().split())
v = sorted([int(input()) for _ in range(n)])
a = sum(v)
while a > s and n:
    a -= v.pop()
    n -= 1
print(n)
