n = input()
if n.find('f') != -1:
    if n.find('f') == n.rfind('f'):
        print(-1)
    else:
        print(n.find('f', n.find('f') + 1))
elif n.find('f') == -1:
    print(-2)
