import time
input()
swp_count = 0
nums = [int(item) for item in input().split(' ')]
nums2 = nums.copy()

# brute force (too slow for some test cases):
t0 = time.clock()
for i in range(len(nums2)):
    if nums2[i] == i+1:
        pass
    else:
        swp_count += 1
        swp_pos = nums2.index(i+1, i+1, len(nums2))
        nums2[i], nums2[swp_pos] = nums2[swp_pos], nums2[i]

# dynamic programming:
val_dict = {}
swp_count = 0
swp_idx = -1
stp_idx = 0
t1 = time.clock()
for i in range(len(nums)):
    if nums[i] == i+1:
        pass
    else:
        swp_count += 1

        try:
            swp_idx = val_dict[i+1]
        except:
            for j in range(stp_idx, len(nums)):
                val_dict[nums[j]] = j
                if nums[j] == i+1:
                    swp_idx = j
                    stp_idx = j
                    break
        finally:
            nums[swp_idx], nums[i] = nums[i], nums[swp_idx]
            val_dict[i+1] = i
            val_dict[nums[swp_idx]] = swp_idx

t_end = time.clock()

print(f'algo1: {t_end-t0}')
print(f'algo2: {t_end-t1}')

print(swp_count)

# Test case (not in the default 3 test cases on Hackerrank):
# in:
# 10
# 3 7 6 9 1 8 10 4 2 5
# out:
# 9