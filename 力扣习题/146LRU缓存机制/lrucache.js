var MNode = /** @class */ (function () {
    function MNode(key) {
        this.key = key;
    }
    return MNode;
}());
var LRUCache = /** @class */ (function () {
    function LRUCache(capacity) {
        this.capacity = capacity;
        this.dict = {};
        this.order = [];
    }
    LRUCache.prototype.get = function (key) {
        if (key in this.dict) {
            var node = this.dict[key].node;
            if (node.front) {
                node.front.back = node.back;
            }
            if (node.back) {
                node.back.front = node.front;
            }
            node.front = this.order[this.order.length - 1];
            node.back = undefined;
            return this.dict[key].value;
        }
        else {
            return -1;
        }
    };
    LRUCache.prototype.put = function (key, value) {
        if (key in this.dict) {
            this.dict[key].value = value;
            var node = this.dict[key].node;
            if (node.front) {
                node.front.back = node.back;
            }
            if (node.back) {
                node.back.front = node.front;
            }
            node.front = this.order[this.order.length - 1];
            node.back = undefined;
        }
        else if (this.order.length < this.capacity) {
            var node = new MNode(key);
            node.key = key;
            if (this.order.length != 0) {
                node.front = this.order[this.order.length - 1];
                this.order[this.order.length - 1].back = node;
            }
        }
        else {
            var ok = this.order.shift().key;
            this.order[0].front = undefined;
            delete this.dict[ok];
            var node = new MNode(key);
            node.key = key;
            if (this.order.length != 0) {
                node.front = this.order[this.order.length - 1];
                this.order[this.order.length - 1].back = node;
            }
        }
    };
    return LRUCache;
}());
/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
var obj = new LRUCache(2);
console.log(obj.get(2));
console.log(obj.put(2, 6));
console.log(obj.get(1));
console.log(obj.put(1, 5));
console.log(obj.put(1, 2));
console.log(obj.get(1));
console.log(obj.get(2));
