from math import gcd
input()
rad = [int(item) for item in input().split(' ')]
for item in rad[1:]:
    div = gcd(rad[0], item)
    print(str(int(rad[0]/div))+'/'+str(int(item/div)))