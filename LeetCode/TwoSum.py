# %%
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Easiest implementation is O(n^2): Double for loop, for each index i search rest ([i+1:]) of array
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Faster implementation, use dict to keep track of already seen values
        tracker = {}
        for i, v in enumerate(nums):
            try:
                j = tracker[target-v]
                return [i, j]
            except KeyError:
                pass
            tracker[v] = i


# %%
tmp = Solution()
print(tmp.twoSum([3, 2, 4], 6))
