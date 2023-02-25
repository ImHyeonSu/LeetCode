from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        nums.sort()
        before = nums[0]
        counter = 0
        for i in range(1,len(nums),1):
            if before == nums[i]:
                nums[i] = "_"
            else:
                before = nums[i]
        for i in nums:
            if str( type( i ) ) == "<class 'int'>":
                counter +=1
        return counter

a = Solution()
b = [0,0,1,1,1,2,2,3,3,4]
a.removeDuplicates(b)

'''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        x=nums[0]
        i=0
        while i<len(nums)-1:
            if x==nums[1+i]:
                del nums[1+i]
            else:
                x=nums[1+i]
                i+=1
        return i+1'''