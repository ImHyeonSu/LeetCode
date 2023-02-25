from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0

        for i in range(0,len(nums),1):
            if nums[i] == val:
                nums[i] == -1

        for i in nums:
            if i != -1:
                counter += 1
        return counter

'''  class Solution:
        def removeElement(self, nums: List[int], val: int) -> int:
            if len(nums) == 0:
                return 0

            while val in nums:
                nums.remove(val)    '''
