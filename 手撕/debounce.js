"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.counter = void 0;
const debounce = (fn, delay = 500, immediate = true) => {
    let timeout = null;
    return (...arg) => {
        if (immediate) {
            fn(...arg);
            immediate = false;
        }
        if (timeout) {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                fn(...arg);
            }, delay);
        }
        else {
            timeout = setTimeout(() => {
                fn(...arg);
            }, delay);
        }
    };
};
function counter() {
    let c = 0;
    return () => {
        c++;
        console.log(`执行第 ${c} 次`);
    };
}
exports.counter = counter;
const count = counter();
const dcount = debounce(count, 1000, false);
dcount();
