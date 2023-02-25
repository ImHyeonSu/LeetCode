class Solution:
    def isPalindrome(self, x: int) -> bool:
        return_x = str(x)[::-1]
        if return_x == str(x):
            return True
        else:
            return False
#
