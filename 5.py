import itertools

print(*list(map(lambda x: ''.join(x), itertools.permutations(''.join(map(str, range(1, int(input()) + 1)))))), sep='\n')
