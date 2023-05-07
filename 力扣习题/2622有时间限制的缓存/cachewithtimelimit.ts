class TimeLimitedCache {
    constructor() {
        this.timers = new Map();
        this.val = new Map();
    }

    private timers: Map<number, unknown>;
    private val: Map<number, number>;

    set(key: number, value: number, duration: number): boolean {
        let res = false;
        if (this.timers.has(key)) {
            clearTimeout(this.timers.get(key) as number);
            res = true;
        }
        this.val.set(key, value);
        const timer = setTimeout(() => {
            this.val.delete(key);
            this.timers.delete(key);
        }, duration);
        this.timers.set(key, timer);
        return res;
    }

    get(key: number): number {
        return this.val.get(key) ?? -1;
    }

    count(): number {
        return this.val.size;
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */