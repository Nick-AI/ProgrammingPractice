names = {}
for j in range(int(input())):
    com = input().split()
    if com[0][0] == 'a':
        for idx in range(len(com[1])):
            if idx < len(com[1]):
                try:
                    names[com[1][:idx+1]] += 1
                except:
                    names[com[1][:idx+1]] = 1
    else:
        try:
            print(names[com[1]])
        except:
            print(0)
