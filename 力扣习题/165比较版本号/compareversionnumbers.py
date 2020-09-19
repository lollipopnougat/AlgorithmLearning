class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1,n2 = version1.split('.'), version2.split('.')
        l1, l2 = len(n1), len(n2)
        t = l1 - l2
        if t > 0:
            n2.extend([0] * t)
        else:
            n1.extend([0] * -t)
        while n1 and n2:
            if int(n1[0]) > int(n2[0]):
                return 1
            elif int(n1[0]) < int(n2[0]):
                return -1
            n1.pop(0)
            n2.pop(0)
            continue
        return 0
