a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delt_A = (a * d) - (c * b)
delt_a = (e * d) - (b * f)
delt_b = (a * f) - (c * e)
if delt_A != 0:
    x = delt_a / delt_A
    y = delt_b / delt_A
    if (x - int(x)) != 0 and (y - int(y)) != 0:
        print(x, y)
    elif (x - int(x)) != 0 and (y - int(y)) == 0:
        print(x, int(y))
    elif (x - int(x)) == 0 and (y - int(y)) != 0:
        print(int(x), y)
    else:
        print(int(x), int(y))
