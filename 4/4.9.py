def ReduceFraction(n, m):
    p = max(n, m)
    q = min(n, m)
    if p == q and p * q != 0:
        return 1, 1
    else:
        x = p % q
        while x > 0:
            p = q
            q = x
            x = p % q
        return n // q, m // q
n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
