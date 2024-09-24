# https://leetcode.com/problems/copy-list-with-random-pointer


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        copyOld = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            copyOld[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = copyOld[cur]
            copy.next = copyOld[cur.next]
            copy.random = copyOld[cur.random]
            cur = cur.next

        return copyOld[head]
