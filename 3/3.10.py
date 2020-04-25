x = input()
a = x.find('f')
b = x.rfind('f')
if a != -1 and b != -1:
    if a == b:
        print(a)
    else:
        print(a, b)
