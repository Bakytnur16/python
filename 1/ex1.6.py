n = int(input())
x = n // 3600
y = (n % 3600) // 60
z = (n % 3600) % 60
if x >= 24:
    x = x % 24
if 0 <= y < 10:
    y = '0' + str(y)
if 0 <= z < 10:
    z = '0' + str(z)
print(x, ':', y, ':', z, sep='')