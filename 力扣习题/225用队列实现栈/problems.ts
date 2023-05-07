class MyStack {

    q1: number[];
    q2: number[];
    main = false;
    constructor() {
        this.q1 = [];
        this.q2 = [];
    }

    push(x: number): void {
        if (this.main) {
            this.q1.push(x);
        } else {
            this.q2.push(x);
        }
    }

    pop(): number {
        let res = 0;
        if (this.main) {
            while (this.q1.length > 1) {
                this.q2.push(this.q1.shift() as number);
            }
            res = this.q1.shift() as number;
            this.main = false;
        } else {
            while (this.q2.length > 1) {
                this.q1.push(this.q2.shift() as number);
            }
            res = this.q2.shift() as number;
            this.main = true;
        }
        return res;
    }

    top(): number {
        let res = 0;
        if (this.main) {
            while (this.q1.length > 1) {
                this.q2.push(this.q1.shift() as number);
            }
            res = this.q1[0];
            this.q2.push(this.q1.shift() as number);
            this.main = false;
        } else {
            while (this.q2.length > 1) {
                this.q1.push(this.q2.shift() as number);
            }
            res = this.q2[0];
            this.q1.push(this.q2.shift() as number);
            this.main = true;
        }
        return res;
    }

    empty(): boolean {
        if(this.main) {
            return this.q1.length == 0;

        } else {
            return this.q2.length == 0;
        }
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */