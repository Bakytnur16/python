n = int(input())
x = n // 1000
y = (n % 100 - x) / 10
z = n % 10
e = n // 10 % 10
if (n // 100) == (x * 10 + y):
    print(1)
else:
    print(int(Z * 1000 + e * 100 + y * 10 + x))
