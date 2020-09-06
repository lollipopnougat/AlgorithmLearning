class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
            while i >= 1 and nums1[i] <= nums1[i - 1]:
                nums1[i], nums1[i - 1] = nums1[i - 1], nums1[i]
                i -= 1