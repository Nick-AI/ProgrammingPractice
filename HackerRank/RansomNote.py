# it = [int(num) for num in input().split()]
# if it[1] > it[0]:
#     print("No")
input()
vocab = {}
for word in input().split():
    try:
        vocab[word] += 1
    except:
        vocab[word] = 1
for test in input().split():
    if test not in vocab or vocab[test] < 1:
        print("No")
        exit()
    else:
        vocab[test] -= 1
print("Yes")
