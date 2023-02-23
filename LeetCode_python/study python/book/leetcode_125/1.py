#list를 이용한 방법
class ggg():
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        print(strs)

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

ss = "1331"
g = ggg()
print(g.isPalindrome(ss))