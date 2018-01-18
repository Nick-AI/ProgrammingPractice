import re

inp = input()
str_len = len(inp)
str_sp = str_len - len(inp.replace('_', ''))
str_low = len(re.sub(r'[^a-z]', '', inp))
str_up = len(re.sub(r'[^A-Z]', '', inp))
str_sym = str_len - str_sp - str_low - str_up

print('{:.15g}'.format(str_sp/str_len))
print('{:.15g}'.format(str_low/str_len))
print('{:.15g}'.format(str_up/str_len))
print('{:.15g}'.format(str_sym/str_len))
