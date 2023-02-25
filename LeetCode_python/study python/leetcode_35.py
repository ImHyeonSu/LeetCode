from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        counter = len(nums)//2
        last = 0
        for i in range(0,len(nums),1):
            if nums[i] < target:
                last = nums[i]
            elif nums[i] == target:
                return i

            if nums[i] > target and last < target:
                return i
        if nums[len(nums)-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0

gg = Solution()
print(gg.searchInsert([1,3,5,6], 0))