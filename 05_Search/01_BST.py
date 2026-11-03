class TreeNode:
    def __init__(self, key): 
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):

        if node is None:  # create a new node if the current node is None
            return TreeNode(key)
        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
        else:
            node.right = self.insert_recursive(node.right, key)
        return node  # duplicate key is not inserted in the BST

    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):
        if node is None:  # key not found in the tree
            return node
        # search for the key to be deleted
        if key < node.key:
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)
        
        # key is found, now delete it
        else:
            if node.left is None:  # node to be deleted has only right child
                return node.right
            if node.right is None:  # node to be deleted has only left child
                return node.left
            
            temp = self.find_min(node.right)  # minimum value in the right subtree
            node.key = temp.key  
            # delete a temp node
            node.right = self.delete_recursive(node.right, temp.key)
        return node    

    def find_min(self, node):
        while node.left is not None: # go left until None is found
            node = node.left   
        return node

    def inorder(self):
        self.inorder_recursive(self.root)
        print()

    def inorder_recursive(self, node):  # visit left, root, and right
        if node is not None:
            self.inorder_recursive(node.left)
            print(node.key, end=' ')
            self.inorder_recursive(node.right)


if __name__ == "__main__":
    tree = BST()

    for key in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(key)

    tree.inorder()  # 20 30 40 50 60 70 80        

    tree.delete(20) # Delete leaf node
    tree.inorder()  # 30 40 50 60 70 80

    tree.delete(30) # Delete node with one child
    tree.inorder()  # 40 50 60 70 80

    tree.delete(50) # Delete node with two children
    tree.inorder()  # 40 60 70 80    