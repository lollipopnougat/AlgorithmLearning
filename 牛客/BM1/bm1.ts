import { ListNode } from '../utils';


/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 
 * @param head ListNode类 
 * @return ListNode类
 */
export function ReverseList(head: ListNode): ListNode {
    // write code here
    let rh: ListNode | null;
    if (head) {
        if (head.next) {
            let p = ReverseList(head.next);
            rh = p;
            while (p && p.next) {
                p = p.next;
            }
            p.next = head;
            head.next = null;
            return rh;
        }
    }
    return head;
}

let list = ListNode.fromStringBuildList('[1,2,3,4,5]');
let list2 = ListNode.fromStringBuildList('[1,2,3,4,5]');
let list3 = ListNode.fromStringBuildList('[7,7,3,4,7,7,7,7,7,7,7,5]');
let list4 = ListNode.fromStringBuildList('[1,2,6,6,5,5,5,5]');
let res = ReverseList(list);
let res2 = ReverseList(list2);
let res3 = ReverseList(list3);
let res4 = ReverseList(list4);
let ress = ListNode.ListToString(res);
console.log(ress);
console.log(ListNode.ListToString(res2));
console.log(ListNode.ListToString(res3));
console.log(ListNode.ListToString(res4));