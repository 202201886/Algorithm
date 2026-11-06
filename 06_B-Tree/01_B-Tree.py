class TreeNode:
    def __init__(self):
        self.keys = []
        self.children = []
        self.parent = None

class BTree:
    def __init__(self):
        self.root = TreeNode()
        self.max_keys = 5

    def find_leaf(self, node, key):  # find the leaf node to insert the key
        if len(node.children) == 0:
            return node

        index = 0

        while index < len(node.keys) and key > node.keys[index]:
            index += 1

        return self.find_leaf(node.children[index], key)

    def insert(self, key):  # find the leaf node
        leaf_node = self.find_leaf(self.root, key)

        # check duplicate keys
        if key in leaf_node.keys:
            return

        # insert the key in sorted order
        leaf_node.keys.append(key)
        leaf_node.keys.sort()

        # check overflow
        if len(leaf_node.keys) > self.max_keys:
            self.clear_overflow(leaf_node)

    def clear_overflow(self, node):
        # find the middle key
        middle_index = len(node.keys) // 2
        middle_key = node.keys[middle_index]

        # split the node
        right_node = TreeNode()
        right_node.keys = node.keys[middle_index + 1:]
        node.keys = node.keys[:middle_index]

        # move the children
        if len(node.children) > 0:
            right_node.children = node.children[middle_index + 1:]
            node.children = node.children[:middle_index + 1]

            for child_node in right_node.children:
                child_node.parent = right_node

        # check if the root has overflow
        if node.parent is None:
            new_root = TreeNode()
            new_root.keys.append(middle_key)
            new_root.children = [node, right_node]

            node.parent = new_root
            right_node.parent = new_root

            self.root = new_root

        else:
            parent_node = node.parent

            # find the position of the node
            index = parent_node.children.index(node)

            # insert the middle key into the parent
            parent_node.keys.insert(index, middle_key)
            parent_node.children.insert(index + 1, right_node)
            right_node.parent = parent_node

            # check overflow in the parent node
            if len(parent_node.keys) > self.max_keys:
                self.clear_overflow(parent_node)

    def inorder(self):
        # print the keys in sorted order
        self.inorder_recursive(self.root)
        print()

    def inorder_recursive(self, node):
        # visit the children and keys in order
        for index in range(len(node.keys)):
            if len(node.children) > 0:
                self.inorder_recursive(node.children[index])

            print(node.keys[index], end=' ')

        if len(node.children) > 0:
            self.inorder_recursive(node.children[-1])

    def print_tree(self, node=None, level=0):
        # print the tree structure
        if node is None:
            node = self.root

        print("  " * level + str(node.keys))

        for child_node in node.children:
            self.print_tree(child_node, level + 1)


if __name__ == "__main__":
    tree = BTree()

    for key in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        tree.insert(key)

    tree.print_tree()

    tree.inorder()