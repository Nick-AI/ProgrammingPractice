import math
for i in range(int(input())):
    vals = [float(item) for item in input().split(' ')]
    t = vals[2] / vals[0] / math.cos(math.radians(vals[1]))
    y = vals[0] * t * math.sin(math.radians(vals[1]))-0.5*9.81*t**2
    if y-1 > vals[3] and y+1 < vals[4]:
        print('Safe')
    else:
        print('Not Safe')
