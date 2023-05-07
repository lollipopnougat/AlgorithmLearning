export { };

type F = (...p: any[]) => any

function debounce(fn: F, t: number): F {
    let timer: unknown | null = null;
    return function (...args) {
        if (timer) {
            clearTimeout(timer as number);
        }
        timer = setTimeout(() => {
            fn.apply(this, args);
        }, t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */