class Node:
    def __init__(self, key, value):
        self.key = key #The key used in the cache dictionary
        self.value = value # The value associated with the key
        self.prev = None #Pointer to the previous node in the list
        self.next = None # Pointer to the next node in the list

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity # maximum number of items the cache can hold
        self.cache = {} #Dictionary to store key -> node mappings for O(1) access

        #Create two dummy nodes to simplify adding/removing nodes (head = most recent, tail = least)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        #Connect head and tail to each other
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        node.prev = self.head #Point back to head
        node.next = self.head.next # Point forward to the former first node
        self.head.next.prev = node #Update the former first node to point back to new node
        self.head.next = node #Head now points forward to the new node

    def remove_node(self, node):
        prev = node.prev #Get the node before the one we’re removing
        nxt = node.next # Get the node after the one we’re removing
        prev.next = nxt # Skip over the node being removed
        nxt.prev = prev #Skip over the node in the other direction too

    def move_to_front(self, node):
        self.remove_node(node) #Take it out of its current spot
        self.add_to_front(node) #Put it right after the head

    def get(self, key):
        if key in self.cache: #Check if the key exists
            node = self.cache[key] #Get the corresponding node
            self.move_to_front(node) # Since it was just used, move it to front
            return node.value
        return None  #not found? return None

    def set(self, key, value):
        if key in self.cache: # If the key exists, update the value and move it to the front
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity: # If the key doesn't exist and cache is full, remove the least recently used item
                lru = self.tail.prev #Least Recently Used is just before the dummy tail
                self.remove_node(lru)
                del self.cache[lru.key] #Remove it from the dictionary

            new_node = Node(key, value) # Add new node to the front and to the dictionary
            self.add_to_front(new_node)
            self.cache[key] = new_node


cache = LRUCache(2)
cache.set(1, 'A')       # Cache: {1:'A'}
cache.set(2, 'B')       # Cache: {1:'A', 2:'B'}
print(cache.get(1))     # Should return 'A' and make 1 most recently used
cache.set(3, 'C')       # Evicts key 2 (least recently used)
print(cache.get(2))     # Should return None
print(cache.get(3))     # Should return 'C'
cache.set(4, 'D')       # Evicts key 1
print(cache.get(1))     # Should return None
print(cache.get(4))     # Should return 'D'
