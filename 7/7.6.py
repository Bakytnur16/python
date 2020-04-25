x = set()
common = set()
for i in range(int(input())):
    a = {input() for j in range(int(input()))}
    common.update(a)
    if i == 1:
        x.update(a)
    else:
        x &= a
print(len(x))
print('\n'.join(sorted(x)))
print(len(common))
print('\n'.join(sorted(common)))
