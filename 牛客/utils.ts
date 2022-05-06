export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
    static fromStringBuildList(str: string): ListNode {
        let strs = str.substring(1, str.length - 1).trim().split(',');
        let head = new ListNode();
        let p = head;
        for (let i of strs) {
            let val = parseInt(i);
            p.next = new ListNode(val);
            p = p.next;
        }
        return head.next as ListNode;
    }
    static ListToString(node: ListNode): string {
        let strs: string[] = [];
        let p: ListNode | null = node;
        while (p) {
            strs.push(`${p.val}`);
            p = p.next;
        }
        return strs.join(',');
    }
}
