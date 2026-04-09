/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        /**
           One fast pontier move 2 times 
           one slow pointe remove 1 time             
        **/
        if(head == null) return false;

        ListNode curr = head.next;
        ListNode prev = null;

        while(curr != null && curr.next != null){
            if(curr == prev)
                return true;
            curr = curr.next.next;
            if(prev == null){
                prev = head;
            }else{
                prev = prev.next;
            }
        }

        return false;
    }
}
