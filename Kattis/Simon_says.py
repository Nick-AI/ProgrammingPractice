reps = int(input())

for _ in range(reps):
    inp = input()
    if inp[:11] == 'simon says ':
        print(inp[11:])
    else:
        print()
