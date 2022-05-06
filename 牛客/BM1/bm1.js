"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ReverseList = void 0;
const utils_1 = require("../utils");
/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param head ListNode类
 * @return ListNode类
 */
function ReverseList(head) {
    // write code here
    let rh;
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
exports.ReverseList = ReverseList;
let list = utils_1.ListNode.fromStringBuildList('[1,2,3,4,5]');
let list2 = utils_1.ListNode.fromStringBuildList('[1,2,3,4,5]');
let list3 = utils_1.ListNode.fromStringBuildList('[7,7,3,4,7,7,7,7,7,7,7,5]');
let list4 = utils_1.ListNode.fromStringBuildList('[1,2,6,6,5,5,5,5]');
let res = ReverseList(list);
let res2 = ReverseList(list2);
let res3 = ReverseList(list3);
let res4 = ReverseList(list4);
let ress = utils_1.ListNode.ListToString(res);
console.log(ress);
console.log(utils_1.ListNode.ListToString(res2));
console.log(utils_1.ListNode.ListToString(res3));
console.log(utils_1.ListNode.ListToString(res4));
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiYm0xLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiYm0xLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7OztBQUFBLG9DQUFvQztBQUdwQzs7Ozs7R0FLRztBQUNILFNBQWdCLFdBQVcsQ0FBQyxJQUFjO0lBQ3RDLGtCQUFrQjtJQUNsQixJQUFJLEVBQW1CLENBQUM7SUFDeEIsSUFBSSxJQUFJLEVBQUU7UUFDTixJQUFJLElBQUksQ0FBQyxJQUFJLEVBQUU7WUFDWCxJQUFJLENBQUMsR0FBRyxXQUFXLENBQUMsSUFBSSxDQUFDLElBQUksQ0FBQyxDQUFDO1lBQy9CLEVBQUUsR0FBRyxDQUFDLENBQUM7WUFDUCxPQUFPLENBQUMsSUFBSSxDQUFDLENBQUMsSUFBSSxFQUFFO2dCQUNoQixDQUFDLEdBQUcsQ0FBQyxDQUFDLElBQUksQ0FBQzthQUNkO1lBQ0QsQ0FBQyxDQUFDLElBQUksR0FBRyxJQUFJLENBQUM7WUFDZCxJQUFJLENBQUMsSUFBSSxHQUFHLElBQUksQ0FBQztZQUNqQixPQUFPLEVBQUUsQ0FBQztTQUNiO0tBQ0o7SUFDRCxPQUFPLElBQUksQ0FBQztBQUNoQixDQUFDO0FBaEJELGtDQWdCQztBQUVELElBQUksSUFBSSxHQUFHLGdCQUFRLENBQUMsbUJBQW1CLENBQUMsYUFBYSxDQUFDLENBQUM7QUFDdkQsSUFBSSxLQUFLLEdBQUcsZ0JBQVEsQ0FBQyxtQkFBbUIsQ0FBQyxhQUFhLENBQUMsQ0FBQztBQUN4RCxJQUFJLEtBQUssR0FBRyxnQkFBUSxDQUFDLG1CQUFtQixDQUFDLDJCQUEyQixDQUFDLENBQUM7QUFDdEUsSUFBSSxLQUFLLEdBQUcsZ0JBQVEsQ0FBQyxtQkFBbUIsQ0FBQyxtQkFBbUIsQ0FBQyxDQUFDO0FBQzlELElBQUksR0FBRyxHQUFHLFdBQVcsQ0FBQyxJQUFJLENBQUMsQ0FBQztBQUM1QixJQUFJLElBQUksR0FBRyxXQUFXLENBQUMsS0FBSyxDQUFDLENBQUM7QUFDOUIsSUFBSSxJQUFJLEdBQUcsV0FBVyxDQUFDLEtBQUssQ0FBQyxDQUFDO0FBQzlCLElBQUksSUFBSSxHQUFHLFdBQVcsQ0FBQyxLQUFLLENBQUMsQ0FBQztBQUM5QixJQUFJLElBQUksR0FBRyxnQkFBUSxDQUFDLFlBQVksQ0FBQyxHQUFHLENBQUMsQ0FBQztBQUN0QyxPQUFPLENBQUMsR0FBRyxDQUFDLElBQUksQ0FBQyxDQUFDO0FBQ2xCLE9BQU8sQ0FBQyxHQUFHLENBQUMsZ0JBQVEsQ0FBQyxZQUFZLENBQUMsSUFBSSxDQUFDLENBQUMsQ0FBQztBQUN6QyxPQUFPLENBQUMsR0FBRyxDQUFDLGdCQUFRLENBQUMsWUFBWSxDQUFDLElBQUksQ0FBQyxDQUFDLENBQUM7QUFDekMsT0FBTyxDQUFDLEdBQUcsQ0FBQyxnQkFBUSxDQUFDLFlBQVksQ0FBQyxJQUFJLENBQUMsQ0FBQyxDQUFDIn0=