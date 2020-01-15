class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        length = 0
        for i in range(l):
            for j in range(i,l):
                pass

    def reMain(self,s:str) -> int:
        l = len(s)
        length = 0
        for i in range(l):
            for j in range(i,l):
                if s[i] == s[j]:
                    length = self.reMain(s[i:])
        