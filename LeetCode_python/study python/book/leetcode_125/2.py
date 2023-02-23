#deque를 이용한 방법
import collections
from typing import Deque


class ggg():
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        print(strs)

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

ss = "1331"
g = ggg()
print(g.isPalindrome(ss))