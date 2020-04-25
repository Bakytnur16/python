fin = open('input.txt', 'r', encoding='utf-8')
a = fin.read().strip().split()
text = dict()
for n in a:
    text[n] = text.get(n, 0) + 1
print(max(sorted(text.keys()), key=lambda x: text[x]))
fin.close()
