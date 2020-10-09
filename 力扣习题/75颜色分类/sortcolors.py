class Solution:
    def sortColors(self, nums: list) -> None:
        """
        记录012个数
        """
        m = [0, 0, 0]
        for i in nums:
            m[i] += 1
        l = len(nums)
        i = 0
        while i < l:
            if m[0] > 0:
                nums[i] = 0
                m[0] -= 1
            elif m[1] > 0:
                nums[i] = 1
                m[1] -= 1
            else:
                nums[i] = 2
            i += 1


class Solution2:
    def sortColors(self, nums: list) -> None:
        """
        快排改良法
如果使用普通的快排划分，虽然时间复杂度是O(nlogn)，空间复杂度是O(1)。

但是仍然不是最优解。因为普通的快排划分需要对数组进行两次扫描(第一次以2为中心划分，第二次以1为中心划分)。

题目要求的最优是对数组进行一次扫描。

怎么做呢？

设置两个变量r1,r2，含义是r1,左边(包含r1)的变量值都小于1，r2左边(包含r2)的变量值都小于2。

那么初始时他俩都是-1(实际上是左边界-1)，代表他俩所包裹的范围是空。

假设现在有数组nums = [0,0,1,1,2,0,0],r1 = 1,r2 = 3。下一个数组索引i是5，也就是要处理0，这个数是小于2的。

因此r2+1，代表区间扩大，把nums[i]和nums[r2]交换。此时维持了r2左侧的数都是小于2的这个性质。

交换完之后，这个小于2的数存放在了nums[r2]，但是这个nums[r2]仍然有可能小于1，若是小于1，那么

应该把r1+1，代表区间扩大，然后把nums[r1]和nums[r2]交换，这样才能维持r1左侧的数小于1的这个性质。
        """
        i = j = -1
        for k in range(len(nums)):
            if nums[k] < 2:
                j += 1
                nums[k], nums[j] = nums[j], nums[k]
                if nums[j] < 1:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

class Solution3:
    def sortColors(self, nums: list) -> None:
        """
        三指针
        """
        l, h = 0, len(nums) - 1
        i = 0
        while i <= h:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 1:
                i += 1
            elif i <= h and nums[i] == 2:
                nums[i], nums[h] = nums[h], nums[i]
                h -= 1