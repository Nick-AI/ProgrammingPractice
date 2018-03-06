import re
it = int(input())
alph = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(it):
    temp = input().lower()
    re.sub(r'[^a-z]', '', temp)
    missing = ''
    for letter in alph:
        if letter not in temp:
            missing += letter
    if len(missing) == 0:
        print('pangram')
    else:
        print('missing', str(missing))