class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity =  capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

def add_to_front(self, node):
    node.prev = self.head
    node.next = self.head.next

    self.head.next.prev = node
    self.head.next = node

def remove_node(self, node):
    prev = node.prev
    nxt = node.next

    prev.next = nxt
    nxt.prev = prev

