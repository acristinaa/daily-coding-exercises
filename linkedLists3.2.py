class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
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

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

def build_linked_list(digits):
    dummy = ListNode(0)
    current = dummy
    for d in digits:
        current.next = ListNode(d)
        current = current.next
    return dummy.next

def print_linked_list(node):
    digits = []
    while node:
        digits.append(str(node.val))
        node = node.next
    print(" -> ".join(digits))

# ----- TEST -----


l1 = build_linked_list([9, 9])
l2 = build_linked_list([5, 2])


result = addTwoNumbers(l1, l2)


print("Result:")
print_linked_list(result)
