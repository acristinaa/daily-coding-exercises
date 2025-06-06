class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rearrange_list(head):
    if not head or not head.next:
        return head

    is_less = True  # Start with expecting a '<' relation

    current = head
    while current.next:
        if is_less:
            if current.val > current.next.val:
                # Swap values to satisfy '<'
                current.val, current.next.val = current.next.val, current.val
        else:
            if current.val < current.next.val:
                # Swap values to satisfy '>'
                current.val, current.next.val = current.next.val, current.val
        current = current.next
        is_less = not is_less  # Alternate expectation

    return head

# Helper to print list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Helper to create linked list from list
def create_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example usage:
head = create_list([1, 2, 3, 4, 5])
print("Before:")
print_list(head)

head = rearrange_list(head)

print("After:")
print_list(head)
