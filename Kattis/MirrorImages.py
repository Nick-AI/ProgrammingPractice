it = int(input())
for i in range(it):
    out = []
    dims = [int(item) for item in input().split(' ')]
    for row in range(dims[0]):
        out = [input()[::-1]] + out
    print('Test', i+1)
    for item in out:
        print(item)
