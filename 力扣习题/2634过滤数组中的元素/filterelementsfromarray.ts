function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    const res: number[] = [];
    arr.forEach((v, i) => {
        if (fn(v, i)) {
            res.push(v);
        }
    });
    return res;
};