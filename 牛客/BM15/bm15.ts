import { ListNode } from '../utils';
/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 * 
 * @param head ListNode类 
 * @return ListNode类
 */
export function deleteDuplicates(head: ListNode): ListNode {
    // write code here
    let h = head;
    let last_val: number | null = null;
    let p: ListNode | null = head;
    let q = p;
    while (p) {
        if (last_val != null && last_val == p.val) {
            q.next = p.next
        }
        else {
            last_val = p.val;
            q = p;
        }
        p = p.next;
    }
    return h;
}


let list = ListNode.fromStringBuildList('{-50,-49,-49,-49,-48,-48,-47,-47,-46,-46,-46,-44,-42,-40,-40,-40,-39,-39,-38,-37,-36,-36,-35,-34,-33,-33,-32,-31,-31,-29,-22,-22,-21,-19,-16,-15,-15,-14,-14,-12,-11,-11,-9,-7,-7,-7,-6,-6,-3,-1,-1,0,0,1,1,3,3,3,3,4,4,5,6,6,7,8,8,9,9,9,10,12,12,13,15,18,18,19,19,20,21,22,25,29,31,31,32,34,34,35,35,35,36,37,39,39,39,41,41,41,42,43,44,44,45,45,46,46,48,49,49,50}');
let res = deleteDuplicates(list);
let ress = ListNode.ListToString(res);
console.log(ress);