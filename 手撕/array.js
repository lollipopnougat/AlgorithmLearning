"use strict";
function reduce(arr, func, initV) {
    let res = initV;
    arr.forEach(e => {
        res = func(res, e);
    });
    return res;
}
function filter(arr, func) {
    const res = [];
    arr.forEach(e => {
        if (func(e)) {
            res.push(e);
        }
    });
    return res;
}
function map(arr, func) {
    const res = [];
    arr.forEach(e => {
        res.push(func(e));
    });
    return res;
}
const arr = [1, 2, 3, 4, 5];
console.log(reduce(arr, (res, v) => res + v, 0));
console.log(filter(arr, e => e > 2));
console.log(map(arr, e => e + 2));
