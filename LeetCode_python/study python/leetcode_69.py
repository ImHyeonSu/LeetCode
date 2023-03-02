class Solution:
    def mySqrt(self, x: int) -> int:
        if x >= 1 and x < 4:
            return 1
        elif x == 0:
            return 0
        result = 0
        while (result**2 <= x):
            result+=1
        return result-1


gg = Solution()
print(gg.mySqrt(2147395599))
