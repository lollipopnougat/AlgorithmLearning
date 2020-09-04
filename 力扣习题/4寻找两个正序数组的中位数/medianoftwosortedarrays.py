class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        l1, l2 = len(nums1), len(nums2)
        l = l1 + l2
        p, q = 0, 0
        tmp = 0
        while p + q < (l + 1) // 2:
            if p < l1 and q < l2:
                if nums1[p] < nums2[q]:
                    p += 1
                    tmp = nums1[p - 1]
                else:
                    q += 1
                    tmp = nums2[q - 1]
            elif p < l1:
                p += 1
                tmp = nums1[p - 1]
            elif q < l2:
                q += 1
                tmp = nums2[q - 1]
        if l % 2 == 0:
            if p < l1 and q < l2:
                if nums1[p] < nums2[q]:
                    tmp += nums1[p]
                else:
                    tmp += nums2[q]
            elif p < l1:
                tmp += nums1[p]
            elif q < l2:
                tmp += nums2[q]
            tmp /= 2 
        return tmp



