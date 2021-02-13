import itertools
from functools import reduce

k, m = input().split()
lines = list()
for i in range(int(k)):
    lines.append([int(x) for x in input().split(' ')[1:]])
current_max = 0
maxes_list = list(itertools.product(*lines))
for maxes in maxes_list:
    magnitude = sum(map(lambda i: i * i, maxes)) % int(m)
    if magnitude > current_max:
        current_max = magnitude
print(current_max)
