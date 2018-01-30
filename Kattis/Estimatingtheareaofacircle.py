import math
vals = [float(item) for item in input().split(' ')]

while(vals[0] != 0.):
    print(math.pi * vals[0]**2, end=' ') #true_area
    print(((vals[0]*2)**2)*(vals[2]/vals[1])) #est_area
    vals = [float(item) for item in input().split(' ')]