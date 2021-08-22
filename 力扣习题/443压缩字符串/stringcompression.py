from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        le = len(chars)
        if le == 1:
            return 1
        i = 1
        count = 1
        while i < len(chars):
            while i < len(chars) and chars[i] == chars[i - 1]:
                chars.pop(i)
                count += 1
            if count == 1:
                i += 1
                continue
            ins = str(count)
            count = 1
            tl = len(ins)
            c = 0
            while c < tl:
                chars.insert(i, ins[c])
                i += 1
                c += 1
            i += 1
        return len(chars)

    def compress2(self, chars: List[str]) -> int:
        # 三指针法 36ms
        le = len(chars)
        if le == 1:
            return 1
        p = l = r = 0 
        while r < le and l < le:
            while r < le and chars[r] == chars[l]:
                r += 1
            chars[p] = chars[l]
            p += 1
            if r - l == 1:
                l = r
                continue
            ins = str(r - l)
            l += 1
            tl = len(ins)
            c = 0
            while c < tl:
                chars[p] = ins[c]
                c += 1
                p += 1
            l = r
        return p
        

s = Solution()

li = ["a","a","b","b","c","c","c"]
li2 = ["a","a","b","b","a","c","c","d","d","d","d","d"]
li3 = ["a"]
li4 = ["a","b","b"]
li6 = ["a","b","b","b"]
li5 = ["a","a","a","a","a","b"]
l = li2
tmp = s.compress2(l)
print(tmp)
print([l[i] for i in range(tmp)])
