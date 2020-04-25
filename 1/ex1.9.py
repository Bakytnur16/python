h = int(input())
a = int(input())
b = int(input())
day = (h - b) / (a - b)
if (h - b) % (a - b) == 0:
    print(int(day))
else:
    print(int(day) + 1)
