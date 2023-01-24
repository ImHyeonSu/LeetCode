from typing import List


class gg():
    def twoSum(self,nums:List[int], target: int) -> List[int]:
        nums_map = {}
        for i,n in enumerate(nums):
            nums_map[n] = i
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target-n]:
                print(n)
                print(nums_map)
                print(nums_map[target-n])
                return [i, nums_map[target-n]]



g = gg()

nums = [2,7,11,15]
target = 9
print(g.twoSum(nums,target))