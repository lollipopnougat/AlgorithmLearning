function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const res: number[] = [];
    arr.forEach((v, i) => {
        res.push(fn(v, i));
    });
    return res;
};