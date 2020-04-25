n = int(input())
if n <= 10 ** 7:
    x = n // 60
    a = n - x * 60
    if x <= 23 and a <= 59:
        print(x, a)
    else:
        print(x % 24, a % 60)
