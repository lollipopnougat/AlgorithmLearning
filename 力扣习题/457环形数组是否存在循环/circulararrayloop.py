import typing


from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        nxt = lambda x : (x + nums[x]) % n

        for i in range(n):
            if nums[i] == 0: 
                continue
            slow = i
            fast = nxt(i)

            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nxt(fast)] > 0:
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    else:
                        return True
                slow = nxt(slow)
                fast = nxt(nxt(fast))
            while nums[i] > 0:
                tmp = nxt(i)
                nums[i] = 0 
                i = tmp
        return False


class Solution2:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        le = len(nums)
        for i in range(le):
            vis = set()
            j = i
            l = 1
            vis.add(i)
            flag = True if nums[i] > 0 else False
            j = (i + nums[i]) % le
            while j != i:
                if j in vis:
                    l = 1
                    break
                if (nums[j] > 0 and not flag) or (nums[j] < 0 and flag):
                    l = 1
                    break
                else:
                    vis.add(j)
                    j = (j + nums[j]) % le
                    l += 1
            if l > 1:
                return True
        return False

s = Solution()

print(s.circularArrayLoop([2,-1,1,2,2]))
print(s.circularArrayLoop([1,2]))
print(s.circularArrayLoop([1]))
print(s.circularArrayLoop([1,1]))
print(s.circularArrayLoop([-1,1]))
print(s.circularArrayLoop([-2,1,-1,-2,-2]))