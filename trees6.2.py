class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder: #base case: if either list is empty, there's no tree/subtree to build
        return None #return None to represent no node

    root_val = preorder[0] #first item in preorder is always the root of the (sub)tree

    root = TreeNode(root_val) #create the root node using that value

    index = inorder.index(root_val) #this splits the list into left and right subtrees

   
    left_inorder = inorder[:index] #all nodes to the left of the root in inorder are in the left subtree
    right_inorder = inorder[index+1:] #all nodes to the right of the root in inorder are in the right subtree

    left_preorder = preorder[1: 1 + len(left_inorder)] #we take exactly as many elements as the left_inorder has
    right_preorder = preorder[1 + len(left_inorder):] #he rest of the preorder list goes to the right subtree

    #Recursively build the subtrees
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root

preorder = ['A', 'B', 'D', 'E', 'C', 'F']
inorder = ['D', 'B', 'E', 'A', 'C', 'F']


root = build_tree(preorder, inorder)


def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.val)
    print_tree(node.right)

# This should print: D B E A C F
print_tree(root)