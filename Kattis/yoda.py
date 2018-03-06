num1 = input()
num2 = input()
out1 = ''
out2 = ''
while len(num1)<len(num2):
    num1 = '0'+num1
while len(num2)<len(num1):
    num2 = '0'+num2
comb = zip(num1, num2)
for item in comb:
    i1=item[0]
    i2=item[1]
    if i1>i2:
        out1 += i1
    elif i2>i1:
        out2 += i2
    else:
        out1 += i1
        out2 += i2
if len(out1) == 0:
    print('YODA')
else:
    print(int(out1))
if len(out2) == 0:
    print('YODA')
else:
    print(int(out2))