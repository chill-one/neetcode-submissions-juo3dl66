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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        /**
            1 -> 2 -> 4
                         c1

            3 -> 4 -> 5
                         c2

            dummyNode -> 1 -> 2 -> 3 -> 4 -> 4 -> 5
                                                  t
        **/

        ListNode dummyNode = new ListNode();
        ListNode temp = dummyNode;

        ListNode curr1 = list1;
        ListNode curr2 = list2;

        while(curr1 != null && curr2 != null){
            if(curr1.val <= curr2.val){
                temp.next = curr1;
                curr1 = curr1.next;
            }else if(curr1.val > curr2.val){
                temp.next = curr2;
                curr2 = curr2.next;
            }
            temp = temp.next;
        }

        while(curr1 != null){
            temp.next = curr1;
            curr1 = curr1.next;
            temp = temp.next;
        }

        while(curr2 != null){
            temp.next = curr2;
            curr2 = curr2.next;
            temp = temp.next;
        }

        return dummyNode.next;
    }
}