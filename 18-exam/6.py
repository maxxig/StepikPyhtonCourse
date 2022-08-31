import re
with open(input(), 'r') as input_file:
    data = list(map(lambda x: x.rstrip(),input_file.readlines()))

with open('forbidden_words.txt', 'r') as wrong_words_file:
    wrong_words = wrong_words_file.readline().split()
result = []
for d in data:
    for w in wrong_words:
        pattern = re.compile(w, re.IGNORECASE)
        d = pattern.sub('*' * len(w), d)
    result.append(d)
print(*result, sep = '\n')
