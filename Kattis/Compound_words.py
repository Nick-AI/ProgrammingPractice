import itertools
import sys

inp = []
out = set()
for line in sys.stdin:
    inp += line.strip('\n').split(' ')

for item in [item for item in itertools.permutations(inp, 2)]:
    item = ''.join(item)
    if item:
        out.add(item)
        
for item in sorted(out):
    print(item)
