n = int(input())
if n < 10:
    print(0)
else:
    x = int(n / 100)
    a = (n - x * 100) / 10
    print(int(a))
