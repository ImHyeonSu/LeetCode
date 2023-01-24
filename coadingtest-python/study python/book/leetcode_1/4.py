from typing import List


class gg():
    def twoSum(self, nums:List[int], target: int) ->List[int]:
        nums_app = {}
        for i,n in enumerate(nums):
            if target - n in nums_app:
                return [nums_app[target -n], i]
            nums_app[n] = i