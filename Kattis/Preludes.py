import sys

alt_names = {'A#': 'Bb', 'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab'}
for idx, line in enumerate(sys.stdin):
    out = 'UNIQUE'
    line = line.split(' ')
    for key in alt_names:
        if line[0] == key:
            out = alt_names[key]
        elif line[0] == alt_names[key]:
            out = key
    print('Case', str(idx+1) + ':', end=' ')
    if out == 'UNIQUE':
        print(out)
    else:
        print(out, line[1])
