const throttle = (fn: (...args: unknown[]) => unknown, delay = 500, immediate = true): ((...args: unknown[]) => unknown) => {
    let timeout: number | null = null;
    return (...arg: unknown[]) => {
        if (immediate) {
            fn(...arg);
            immediate = false;
        }
        if (timeout) {
            return;
        } else {
            timeout = setTimeout(() => {
                fn(...arg);
                timeout = null;
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
const dcount = throttle(count, 1000, true);
let timeout = setInterval(() => {
    dcount();
}, 500);
setTimeout(() => {
    clearInterval(timeout);
}, 5000);
