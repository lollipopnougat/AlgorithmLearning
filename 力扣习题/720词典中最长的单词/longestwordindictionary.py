class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words.sort(key=len, reverse=True)
        ws = set(words)
        for w in words:
            f = False
            l = len(w)
            for j in range(1, l + 1):
                if w[:j] not in ws:
                    f = False
                    break
                else:
                    f = True
            if f:
                return w
        return ''