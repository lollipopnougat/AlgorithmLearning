class MNode {
    constructor (key: number) {
        this.key = key;
    }
    front?: MNode;
    back?: MNode;
    key: number;
}
interface MData {
    value: number;
    node: MNode;
}

class LRUCache {
    constructor(capacity: number) {
        this.capacity = capacity;
        this.dict = {};
        this.order = [];
    }

    private capacity: number;
    private dict: Record<number, MData>;
    private order: MNode[];

    get(key: number): number {
        if (key in this.dict) {
            let node = this.dict[key].node;
            if(node.front) {
                node.front.back = node.back;
            }
            if(node.back) {
                node.back.front = node.front;
            }
            node.front = this.order[this.order.length - 1];
            node.back = undefined;
            return this.dict[key].value;
        }
        else {
            return -1
        }
    }

    put(key: number, value: number): void {
        if(key in this.dict) {
            this.dict[key].value = value;
            let node = this.dict[key].node;
            if(node.front) {
                node.front.back = node.back;
            }
            if(node.back) {
                node.back.front = node.front;
            }
            node.front = this.order[this.order.length - 1];
            node.back = undefined;
        }
        else if(this.order.length < this.capacity) {
            const node = new MNode(key);
            node.key = key;
            if(this.order.length != 0) {
                node.front = this.order[this.order.length - 1];
                this.order[this.order.length - 1].back = node;
            }
        }
        else {
            let ok = this.order.shift().key;
            this.order[0].front = undefined;
            delete this.dict[ok];
            const node = new MNode(key);
            node.key = key;
            if(this.order.length != 0) {
                node.front = this.order[this.order.length - 1];
                this.order[this.order.length - 1].back = node;
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

const obj = new LRUCache(2)
console.log(obj.get(2))
console.log(obj.put(2, 6))
console.log(obj.get(1))
console.log(obj.put(1, 5))
console.log(obj.put(1, 2))
console.log(obj.get(1))
console.log(obj.get(2))