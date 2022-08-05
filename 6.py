import math
print(2, *list(filter(lambda number: not set(filter(lambda divisor: number % divisor == 0, range(2, int(math.sqrt(number)) + 1))), range(3, int(input())+1, 2))))
