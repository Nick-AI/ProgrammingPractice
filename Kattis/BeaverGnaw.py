import math
d, v = [int(item) for item in input().split(' ')]
while d != 0 and v != 0:
    print('{:.10g}'.format((6*((math.pi*d**3)/4-v)/math.pi-(d**3)/2)**(1/3)))
    d, v = [int(item) for item in input().split(' ')]
