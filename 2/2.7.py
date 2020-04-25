a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a != b and a != c and c != b:
    print(0)
else:
    print(2)
