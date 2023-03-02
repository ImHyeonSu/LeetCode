from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        result = []
        for i in digits:
            a += str(i)
        a = int(a)
        a += 1
        for i in str(a):
            result.append(int(i))
        return result

gg = Solution()
print(gg.plusOne([9]))