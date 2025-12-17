# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to convert a list into a linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list (for output)
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Solution class with the core logic
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# --------- Example Usage ---------
l1_list = [2, 4, 3]  # represents 342
l2_list = [5, 6, 4]  # represents 465

l1 = list_to_linkedlist(l1_list)
l2 = list_to_linkedlist(l2_list)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Convert result back to list and print
print(linkedlist_to_list(result))  # Output: [7, 0, 8]

