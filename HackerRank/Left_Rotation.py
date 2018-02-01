def array_left_rotation(a, n, k):
    temp = a[:k]
    a = a[k:]
    return a + temp


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')