import re
class Solution:
    def __init__(self):
        self.p = re.compile(r'^[+|-]?\d+(?:\.\d+)?(?:[\.|e|E][+|-]?\d+)?$')
    def isNumber(self, s: str) -> bool:
        return True if self.p.search(s) else False

s = Solution()
print(s.isNumber('1'))