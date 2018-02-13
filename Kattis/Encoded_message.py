import math
it = int(input())
for _ in range(it):
    enc = input()
    squ = int(math.sqrt(len(enc)))
    dec = ''
    for i in range(squ-1, -1, -1):
        for j in range(squ):
            dec += enc[i + j * squ]
    print(dec)
