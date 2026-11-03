class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # height of a new node is 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):  # get the height of a node
        if node is None:
            return 0
        return node.height

    def get_difference(self, node):  # get difference between left and right
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):  # right rotation (LL)
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        # renew height after rotation
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):  # left rotation (RR)
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Fix the balance of a node
    def balance_node(self, node):
        balance = self.get_difference(node)

        if balance > 1:  # left subtree is higher
            if self.get_difference(node.left) < 0:
                node.left = self.rotate_left(node.left)  # LR case
            return self.rotate_right(node)  

        if balance < -1:  # right subtree is higher
            if self.get_difference(node.right) > 0:
                node.right = self.rotate_right(node.right)  # RL case
            return self.rotate_left(node) 

        return node

    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):

        if node is None:
            return TreeNode(key)

        # insert the key 
        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self.insert_recursive(node.right, key)
        else:
            return node  # don't insert duplicate keys

        # renew the height after insertion
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # fix the balance
        return self.balance_node(node)

    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):

        if node is None:
            return node

        if key < node.key:  # find the node to delete
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)

        else:  # the node is found
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # find the smallest key in the right subtree
            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self.delete_recursive(node.right, temp.key)

        # renew the height after deletion
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # fix the balance if needed
        return self.balance_node(node)

    def find_min(self, node):
        while node.left is not None:  # go left until None is found
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
    tree = AVLTree()

    for key in [50, 30, 70, 20, 40, 60, 80, 10]:
        tree.insert(key)

    tree.inorder()

    tree.delete(10)
    tree.inorder()

    tree.delete(30)
    tree.inorder()

    tree.delete(50)
    tree.inorder()