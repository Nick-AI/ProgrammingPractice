alph = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
inp = input()
f_half = inp[:int(len(inp)/2)]
s_half = inp[int(len(inp)/2):]

rot_f_half = sum([alph.find(item.lower()) for item in f_half])
rot_s_half = sum([alph.find(item.lower()) for item in s_half])

f_half = [alph.find(alph[alph.find(item.lower())+(rot_f_half%26)]) for item in f_half]
s_half = [alph.find(alph[alph.find(item.lower())+(rot_s_half%26)]) for item in s_half]

out = [alph[f_half[i] + s_half[i]] for i in range(len(f_half))]

print(''.join(out).upper())
