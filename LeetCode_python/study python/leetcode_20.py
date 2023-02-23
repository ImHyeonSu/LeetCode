class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if '()' in s:
                s = s.replace('()', '')
                print(s)
            elif '{}' in s:
                s = s.replace('{}', '')
                print(s)
            elif '[]' in s:
                s = s.replace('[]', '')
                print(s)
            else:
                return not s
aa = Solution()
print(aa.isValid("([)]"))

# {[]} true
# ([)] false