type F = (...args: any[]) => void

function throttle(fn: F, t: number): F {
    let arg: any[] | undefined = undefined;
    let timer: any = null;
    return function (...args) {
        arg = args;
        if (timer) {
            return;
        } else {
            if (args) {
                fn(...args);
                arg = undefined;
            }
            timer = setInterval(() => {
                if (arg) {
                    fn(...arg);
                    arg = undefined;
                } else {
                    clearInterval(timer);
                    timer = null;
                }
            }, t);
        }
    }
};

const throttled = throttle(console.log, 1000);
throttled("log"); // logged immediately.
throttled("log"); // logged at t=100ms.
throttled("log2"); // logged at t=100ms.
throttled("log"); // logged at t=100ms.
throttled("log4"); // logged at t=100ms.
setTimeout(() => {
    throttled('123');
    throttled('122');
    throttled('121');
}, 1500);
