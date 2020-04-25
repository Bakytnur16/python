a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if 0 <= a <= 23 and 0 <= d <= 23:
    if 0 <= b <= 59 and 0 <= c <= 59 and 0 <= e <= 59 and 0 <= f <= 59:
        x = (d * 3600 + e * 60 + f) - (a * 3600 + b * 60 + c)
        print(x)
