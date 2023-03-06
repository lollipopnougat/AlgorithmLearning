function findDisappearedNumbers(nums: number[]): number[] {
    const alphabet = new Set<number>();
    for(let i = 0; i < nums.length; i++) {
        alphabet.add(nums[i]);
    }
    const res: number[] = [];
    for (let i = 1; i < nums.length + 1; i++) {
        if(!alphabet.has(i)) {
            res.push(i)
        }
    }
    return res;
};