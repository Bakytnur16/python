def IsPoint(x, y):
    if (x ** 2 + y ** 2) ** 0.5 <= (2)**0.5:
        return 'YES'
    else:
        return 'NO'
x = float(input())
y = float(input())
print(IsPoint(x, y))
