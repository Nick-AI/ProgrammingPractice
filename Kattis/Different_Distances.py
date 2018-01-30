vals = input()
while(vals != '0'):
    vals = [float(item) for item in vals.split(' ')]
    print('{:.11g}'.format(((abs(vals[0]-vals[2]))**vals[4] + (abs(vals[1]-vals[3]))**vals[4])**(1/vals[4])))
    vals = input()
