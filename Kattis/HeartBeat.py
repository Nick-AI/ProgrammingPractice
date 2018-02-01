for i in range(int(input())):
    vals = [float(item) for item in input().split(' ')]
    a = 60/vals[1]
    b = a*vals[0]
    print('{:.6g} {:.6g} {:.6g}'.format(b-a, b, b+a))
