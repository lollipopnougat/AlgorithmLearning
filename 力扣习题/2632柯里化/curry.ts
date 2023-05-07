function curry(fn: Function): Function {
    const args: number[] = [];
    return function curried(...arg: number[]) {
        args.push(...arg);
        if (args.length == fn.length) {
            return fn(...args);
        }
        return curried;
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */