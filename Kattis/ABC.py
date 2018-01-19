ints = [int(item) for item in input().split(' ')]
keys = {'A': 0, 'B': 1, 'C': 2}
ints.sort()
for letter in input():
    print(ints[keys[letter]], end=' ')
