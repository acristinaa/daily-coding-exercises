class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_intersection_node(headA, headB):
    # Step 1: Find the lengths of both lists
    lenA = 0
    lenB = 0

    currentA = headA
    while currentA is not None:
        lenA += 1 #Count one node
        currentA = currentA.next #Move to the next node

    currentB = headB
    while currentB is not None:
        lenB += 1 #Count one node
        currentB = currentB.next #Move to the next node

    # Step 2: Align the lists
    currentA = headA #Reset currentA to start of list A
    currentB = headB #Reset currentB to start of list B

#Now both currentA and currentB are equally far from the end

    if lenA > lenB:
        for i in range(lenA - lenB): #List A is longer — move currentA forward
            currentA = currentA.val
    else:
        for i in range(lenB - lenA): #List B is longer — move currentB forward
            currentB = currentB.val

    # Step 3: Walk forward together
    while currentA is not None and currentB is not None:
        if currentA == currentB:
            print("Found intersection at:", currentA.val)
            return currentA
        currentA = currentA.next
        currentB = currentB.next

    return None




shared1 = ListNode(8)
shared2 = ListNode(10)
shared1.next = shared2


a1 = ListNode(3)
a2 = ListNode(7)
a1.next = a2
a2.next = shared1  

b1 = ListNode(99)
b2 = ListNode(1)
b1.next = b2
b2.next = shared1  



def print_list(head):
    current = head
    values = []
    while current is not None:
        values.append(str(current.val)) 
        current = current.next
    print(" -> ".join(values)) 

print("List A:")
print_list(a1)

print("List B:")
print_list(b1)

result = get_intersection_node(a1, b1)

if result is not None:
    print("Return: node with value", result.val)
else:
    print("Return: No intersection")
