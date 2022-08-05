import itertools

print(*list(itertools.accumulate(list(map(int, input().split())))))

