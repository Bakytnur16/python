def IsPoint(x, y, xc, yc, r):
    if ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 <= r:
        return 'YES'
    else:
        return 'NO'
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
print(IsPoint(x, y, xc, yc, r))
