function findKthLargest(nums: number[], k: number): number {
    return nums[qSelect(nums, k)];
};

function getIndex(nums: number[], l: number, r: number) {
    const c = nums[l];
    while (l < r) {
        while (l < r && nums[r] >= c) {
            r--;
        }
        nums[l] = nums[r];
        while (l < r && nums[l] <= c) {
            l++;
        }
        nums[r] = nums[l];
    }
    nums[l] = c;
    return l;
}

function qSelect(nums: number[], k: number, l = 0, r = nums.length - 1) {
    if (l < r) {
        const m = getIndex(nums, l, r);
        if (nums.length - k == m) {
            return m;
        }
        if (m > nums.length - k) {
            return qSelect(nums, k, l, m - 1);
        } else if (l == r) {
            return qSelect(nums, k, m + 1, r);

        }
    }
}