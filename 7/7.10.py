inFile = open('input.txt', 'r', encoding='utf-8')
n = []
for l in inFile:
    n += l.strip().split()
words = dict()
for w in n:
    if w in words:
        words[w] += 1
    else:
        words[w] = 0
print(*sorted(words, key=lambda x: (-words[x], x)), sep='\n')
