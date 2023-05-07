export { };

declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function (fn) {
    const res: Record<string, unknown[]> = {};
    this.forEach((v: unknown) => {
        const val = fn(v);
        if (Object.prototype.hasOwnProperty.call(res, val)) {
            res[val].push(v);
        } else {
            res[val] = [v];
        }
    });
    return res;
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */