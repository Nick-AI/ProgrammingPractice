def isValid(s):

    occurences = [0] * 256
    for letter in s:
        occurences[ord(letter)] += 1
    occurences = [item for item in occurences if item != 0]
    max_i = max(occurences)
    min_i = min(occurences)
    if min_i != max_i:
        occ_max = occurences.count(max_i)
        occ_min = occurences.count(min_i)
        if min_i == 1 and occ_min ==1 or max_i == 1 and occ_max == 1:
            return 'YES'
        if max_i - min_i > 1:
            return 'NO'
        if occ_min > 1 and occ_max > 1:
            return 'NO'
    return 'YES'


s = input().strip()
result = isValid(s)
print(result)

