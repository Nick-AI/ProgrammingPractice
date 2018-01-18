it = int(input())
for i in range(it):
    inp = input()
    if inp == 'P=NP':
        print('skipped')
    else:
        print(eval(inp))
