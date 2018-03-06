item = input()
stack = []
for letter in item:
    if letter != '<':
        stack.append(letter)
    else:
        stack.pop()
out = ''
for letter in stack:
    out += letter
print(out)