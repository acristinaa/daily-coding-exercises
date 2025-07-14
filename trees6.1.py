class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root):
    count = [0] #using a list so we can change the number inside

    def is_unival(node):
        if node is None: 
            return True #empty node is considered a unival subtree
        
        #check if left and right subtrees are unival
        left_is_unival = is_unival(node.left)
        right_is_unival = is_unival(node.right)

        #if either the left or right subtree is not unival, this one can't be
        if not left_is_unival or not right_is_unival:
            return False
        
        #if the left child exists and has a different value, it's not unival
        if node.left and node.left.val != node.val:
            return False
        
        #if the right child exists and has a different value, it's not unival
        if node.right and node.right.val != node.val:
            return False
        
        #if we passed all the checks, this subtree is unival.
        count[0] += 1
        return True
    
    is_unival(root)
    return count[0]

        
root = Node(1, 
            Node(1), 
            Node(1, Node(1), Node(1)))

print(count_unival_subtrees(root))  # Should print 5