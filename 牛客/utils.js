"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ListNode = void 0;
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
    static fromStringBuildList(str) {
        let strs = str.substring(1, str.length - 1).trim().split(',');
        let head = new ListNode();
        let p = head;
        for (let i of strs) {
            let val = parseInt(i);
            p.next = new ListNode(val);
            p = p.next;
        }
        return head.next;
    }
    static ListToString(node) {
        let strs = [];
        let p = node;
        while (p) {
            strs.push(`${p.val}`);
            p = p.next;
        }
        return strs.join(',');
    }
}
exports.ListNode = ListNode;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoidXRpbHMuanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyJ1dGlscy50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiOzs7QUFBQSxNQUFhLFFBQVE7SUFHakIsWUFBWSxHQUFZLEVBQUUsSUFBc0I7UUFDNUMsSUFBSSxDQUFDLEdBQUcsR0FBRyxDQUFDLEdBQUcsS0FBSyxTQUFTLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUMsR0FBRyxDQUFDLENBQUE7UUFDeEMsSUFBSSxDQUFDLElBQUksR0FBRyxDQUFDLElBQUksS0FBSyxTQUFTLENBQUMsQ0FBQyxDQUFDLElBQUksQ0FBQyxDQUFDLENBQUMsSUFBSSxDQUFDLENBQUE7SUFDbEQsQ0FBQztJQUNELE1BQU0sQ0FBQyxtQkFBbUIsQ0FBQyxHQUFXO1FBQ2xDLElBQUksSUFBSSxHQUFHLEdBQUcsQ0FBQyxTQUFTLENBQUMsQ0FBQyxFQUFFLEdBQUcsQ0FBQyxNQUFNLEdBQUcsQ0FBQyxDQUFDLENBQUMsSUFBSSxFQUFFLENBQUMsS0FBSyxDQUFDLEdBQUcsQ0FBQyxDQUFDO1FBQzlELElBQUksSUFBSSxHQUFHLElBQUksUUFBUSxFQUFFLENBQUM7UUFDMUIsSUFBSSxDQUFDLEdBQUcsSUFBSSxDQUFDO1FBQ2IsS0FBSyxJQUFJLENBQUMsSUFBSSxJQUFJLEVBQUU7WUFDaEIsSUFBSSxHQUFHLEdBQUcsUUFBUSxDQUFDLENBQUMsQ0FBQyxDQUFDO1lBQ3RCLENBQUMsQ0FBQyxJQUFJLEdBQUcsSUFBSSxRQUFRLENBQUMsR0FBRyxDQUFDLENBQUM7WUFDM0IsQ0FBQyxHQUFHLENBQUMsQ0FBQyxJQUFJLENBQUM7U0FDZDtRQUNELE9BQU8sSUFBSSxDQUFDLElBQWdCLENBQUM7SUFDakMsQ0FBQztJQUNELE1BQU0sQ0FBQyxZQUFZLENBQUMsSUFBYztRQUM5QixJQUFJLElBQUksR0FBYSxFQUFFLENBQUM7UUFDeEIsSUFBSSxDQUFDLEdBQW9CLElBQUksQ0FBQztRQUM5QixPQUFPLENBQUMsRUFBRTtZQUNOLElBQUksQ0FBQyxJQUFJLENBQUMsR0FBRyxDQUFDLENBQUMsR0FBRyxFQUFFLENBQUMsQ0FBQztZQUN0QixDQUFDLEdBQUcsQ0FBQyxDQUFDLElBQUksQ0FBQztTQUNkO1FBQ0QsT0FBTyxJQUFJLENBQUMsSUFBSSxDQUFDLEdBQUcsQ0FBQyxDQUFDO0lBQzFCLENBQUM7Q0FDSjtBQTNCRCw0QkEyQkMifQ==