a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - (4 * a * c)
x1 = (d ** 0.5 - b) / (2 * a)
x2 = (- b - d ** 0.5) / (2 * a)
if a != 0:
    if d > 0:
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
    elif d == 0:
        print(- b / (2 * a))
