from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        j = 0
        for i in pushed:
            st.append(i)
            while j < len(popped) and st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return j == len(popped) 




s = Solution()

l1 = [1, 2, 3, 4, 5]
l2 = [4, 3, 5, 1, 2]
print(s.validateStackSequences(l1, l2))
