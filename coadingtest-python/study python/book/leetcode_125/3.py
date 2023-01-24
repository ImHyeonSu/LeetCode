#간단하고 단순한 방법
import re


class ggg():
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

ss = "1331"
g = ggg()
print(g.isPalindrome(ss))