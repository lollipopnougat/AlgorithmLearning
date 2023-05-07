export { };
type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const cache: Map<string, any> = new Map();
    return function (...args) {
        const argv = args.toString();
        if (cache.has(argv)) {
            return cache.get(argv);
        }
        const res = fn(...args);
        cache.set(argv, res);
        return res;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */