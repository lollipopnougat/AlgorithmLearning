export { };
type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let res = init;
    nums.forEach((v) => {
        res = fn(res, v);
    });
    return res;
};