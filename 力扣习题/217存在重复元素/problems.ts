function containsDuplicate(nums: number[]): boolean {
    const set = new Set<number>();
    for(let i of nums) {
        if (set.has(i)) {
            return true;
        } else {
            set.add(i);
        }
    }
    return false;
};