from collections import Counter
counter = Counter()
with open(r'input.txt', 'rt', encoding = 'utf-8') as file:
    for line in file:
        for word in line.strip().split():
            print(counter[word], end=' ')
            counter[word] += 1
