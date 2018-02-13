alph = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
enc = input().lower()
key = input().lower()
dec = ''

for idx in range(len(enc)):
    shift = alph.find(key[idx])
    tmp = alph.find(enc[idx]) - shift
    key += alph[tmp]
    dec += alph[tmp]
print(dec.upper())
