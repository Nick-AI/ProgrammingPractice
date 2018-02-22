import operator
names = {}
line = input()
while line != '***':
    try:
        names[line] += 1
    except:
        names[line] = 1
    line = input()
names = sorted(names.items(), key=operator.itemgetter(1), reverse=True)
if names[0][1] == names[1][1]:
    print('Runoff!')
else:
    print(names[0][0])
