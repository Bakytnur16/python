import codecs
inFile = open('input.txt', 'r', encoding='utf-8')
name_score = []
for line in inFile:
    line = line.split()
    line.pop(2)
    name_score.append(line)
inFile.close()
name_score.sort()
for i in name_score:
    print(*i)
