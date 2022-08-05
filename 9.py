from functools import reduce
print(*list(map(lambda q: reduce(lambda x, y: (int(x) ^ int(y)), q), zip(*map(lambda j: j.split(), open('input.txt').readlines()[1:])))))

