# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        carry = 0
        curr = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            val = sum % 10

            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next