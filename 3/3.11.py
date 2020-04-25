x = input()
if x.count('h') >= 2:
    print(x[:x.find('h')] + x[x.rfind('h') + 1:])
