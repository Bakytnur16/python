s, n = map(int, (input().split()))
a = sorted([int(input()) for i in range(n)])
b = sum(a)
if b <= s:
    print(n)
elif b > s:
    b = b - a.pop()
    n -= 1
    print(n)
