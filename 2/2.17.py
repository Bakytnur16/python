x = int(input())
max1 = int(input())
max2 = x
while x != 0:
    if x >= max1:
        max2, max1 = max1, x
    elif max2 < x <= max1:
        max2 = x
    x = int(input())
print(max2)
