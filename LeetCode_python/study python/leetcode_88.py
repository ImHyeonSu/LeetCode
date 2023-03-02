from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n >= 1:
            for i in nums2:
                search_n = nums1.index(0)
                nums1[search_n] = i
        nums1.sort()
        print(nums1)

g = Solution()
print(g.merge([0], 0, [1], 1))