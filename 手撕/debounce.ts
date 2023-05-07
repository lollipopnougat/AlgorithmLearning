const debounce = (fn: (...args: unknown[]) => unknown, delay = 500, immediate = true): ((...args: unknown[]) => unknown) => {
    let timeout: number | null = null;
    return (...arg: unknown[]) => {
        if (immediate) {
            fn(...arg);
            immediate = false;
        }
        if (timeout) {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                fn(...arg);
            }, delay);
        } else {
            timeout = setTimeout(() => {
                fn(...arg);
            }, delay);
        }
    };
}

export function counter() {
    let c = 0;
    return () => {
        c++;
        console.log(`执行第 ${c} 次`);
    }
}

const count = counter();
const dcount = debounce(count, 1000, false);
dcount();
