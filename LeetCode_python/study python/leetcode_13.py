class Solution():
    def romanToInt(self, s : str) -> int:
        set_dict = {'I': 1,
                    'IV': 4,
                    'V': 5,
                    'IX': 9,
                    'X': 10,
                    'XL': 40,
                    'L': 50,
                    'XC': 90,
                    'C': 100,
                    'CD': 400,
                    'D': 500,
                    'CM': 900,
                    'M': 1000}
        self.s = list(s)
        before, after = 0, 0
        result = 0
        while len(self.s) > 0:
            for n in set_dict:
                if len(self.s) > 0:
                    before = after
                    after = set_dict[self.s[0]]
                    del self.s[0]
                    if after > before:
                        result += (after-(2*before))
                    else:
                        result += after
        return result

g = Solution()
a = g.romanToInt("III")
print(a)
