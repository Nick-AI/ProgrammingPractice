bats = int(input())
points = [int(item) for item in input().split(' ')]
sum = 0
for item in points:
    if item == -1:
        bats += item
    else:
        sum += item
print(sum/bats)
