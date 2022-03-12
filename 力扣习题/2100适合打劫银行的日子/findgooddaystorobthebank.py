class Solution:
    '''
    dp
    '''
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        l = len(security)
        if l < time * 2:
            return []
        ans = []
        left = [0] * l
        right = [0] * l
        for i in range(1, l):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1
        for i in range(l - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        for i in range(l):
            if left[i] >= time and right[i] >= time:
                ans.append(i)
        return ans