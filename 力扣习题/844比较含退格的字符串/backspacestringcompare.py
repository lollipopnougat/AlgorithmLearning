class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t1 = []
        t2 = []
        for i in s:
            if i == '#' and t1:
                t1.pop()
            elif i != '#':
                t1.append(i)
        for i in t:
            if i == '#' and t2:
                t2.pop()
            elif i != '#':
                t2.append(i)
        return ''.join(t1) == ''.join(t2)


class Solutionn:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t1 = t2 = 0
        l1, l2 = len(s), len(t) 
        i, j = l1 - 1, l2 - 1
        while i >= -1 and j >= -1:
            while i >= 0 and s[i] == '#':
                t1 += 1
                i -= 1
            while j >= 0 and t[j] == '#':
                t2 += 1
                j -= 1
            if t1 > 0 and i >= 0:
                i -= 1
                t1 -= 1
                continue
            if t2 > 0 and j >= 0:
                j -= 1
                t2 -= 1
                continue
            if i > -1 and j > -1 and s[i] != t[j]:
                return False
            else:
                i -= 1
                j -= 1
        return i == j

s = Solutionn()

print(s.backspaceCompare('ab##', 'c#d#'))
print(s.backspaceCompare('ab#', 'cd#'))
print(s.backspaceCompare("y#fo##f", "y#f#o##f"))
