

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 1
        result = 0
        for i in range(0,len(s),1):
            if s[-1] == " ":
                s = s[0 : len(s)-1]
            else:
                if len(s) > 1:
                    result +=1
                    s = s[0 : len(s)-1]
                    if s[-1] == " ":
                        return result
                elif len(s) == 1 and s[-1] != " ":
                    return result + 1




g = Solution()
print(g.lengthOfLastWord("a "))
