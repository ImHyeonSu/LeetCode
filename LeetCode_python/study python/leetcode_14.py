from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = 0
        for i in zip(*strs):
            if len(set(i)) == 1:
                match += 1
            else:
                break
        return strs[0][:match]


g = Solution()
strs = ["flower","flow","flight"]
a = g.longestCommonPrefix(strs)
print(a)
