from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis = abs(target[0]) + abs(target[1])
        for i in ghosts:
            if dis >= abs(i[0] - target[0]) + abs(i[1] - target[1]):
                return False
        return True 