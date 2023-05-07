function reduce<T, R>(arr: T[], func: (res: R, v: T) => R, initV: R): R {
    let res = initV;
    arr.forEach(e => {
        res = func(res, e);
    });
    return res;
}

function filter<T>(arr: T[], func: (e: T) => boolean): T[] {
    const res: T[] = [];
    arr.forEach(e => {
        if(func(e)) {
            res.push(e);
        }
    });
    return res;
}

function map<T, R>(arr: T[], func: (e: T) => R): R[] {
    const res: R[] = [];
    arr.forEach(e => {
        res.push(func(e));
    });
    return res;
}

const arr = [1, 2, 3, 4, 5];

console.log(reduce(arr, (res, v) => res + v, 0));
console.log(filter(arr, e => e > 2));
console.log(map(arr, e => e + 2));
