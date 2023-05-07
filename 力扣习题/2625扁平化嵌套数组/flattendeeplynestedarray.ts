export { };
type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr: MultiDimensionalArray, n: number): MultiDimensionalArray {
    const res: MultiDimensionalArray = [];
    arr.forEach(v => {
        if (n == 0 || typeof v == 'number') {
            res.push(v);
        } else {
            res.push(...flat(v, n - 1));
        }
    });
    return res;
};