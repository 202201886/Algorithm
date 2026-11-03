
class TreeNode:
    def __init__(self, key, color):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    R = "R"
    B = "B"

    def __init__(self):  # create a NIL node
        self.NIL = TreeNode(None, self.B)
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL

    def rotate_right(self, parent_node):  # right rotation
        child_node = parent_node.left
        temp = child_node.right

        # change the node links
        parent_node.left = temp

        if temp != self.NIL:
            temp.parent = parent_node

        child_node.parent = parent_node.parent

        if parent_node.parent == self.NIL:
            self.root = child_node
        elif parent_node == parent_node.parent.right:
            parent_node.parent.right = child_node
        else:
            parent_node.parent.left = child_node

        child_node.right = parent_node
        parent_node.parent = child_node

    def rotate_left(self, parent_node):  # left rotation
        child_node = parent_node.right
        temp = child_node.left

        # change the node links
        parent_node.right = temp

        if temp != self.NIL:
            temp.parent = parent_node

        child_node.parent = parent_node.parent

        if parent_node.parent == self.NIL:
            self.root = child_node
        elif parent_node == parent_node.parent.left:
            parent_node.parent.left = child_node
        else:
            parent_node.parent.right = child_node

        child_node.left = parent_node
        parent_node.parent = child_node

    def insert(self, key):
        # check if the key already exists
        if self.search_recursive(self.root, key) != self.NIL:
            return  # don't insert duplicate keys

        # create a new red node
        new_node = TreeNode(key, self.R)
        new_node.left = self.NIL
        new_node.right = self.NIL

        # find the place to insert the new node
        self.root = self.insert_recursive(self.root, new_node, self.NIL)

        # fix the color after insertion
        self.insert_fixup(new_node)

    def insert_recursive(self, current_node, new_node, parent_node):
        # insert the node when NIL is found
        if current_node == self.NIL:
            new_node.parent = parent_node
            return new_node

        # find the correct position
        if new_node.key < current_node.key:
            current_node.left = self.insert_recursive(
                current_node.left, new_node, current_node)
        else:
            current_node.right = self.insert_recursive(
                current_node.right, new_node, current_node)

        return current_node

    def insert_fixup(self, current_node):
        # fix the tree while the parent is red
        while current_node.parent.color == self.R:

            if current_node.parent == current_node.parent.parent.left:
                uncle_node = current_node.parent.parent.right

                if uncle_node.color == self.R:  # uncle is red
                    current_node.parent.color = self.B
                    uncle_node.color = self.B
                    current_node.parent.parent.color = self.R
                    current_node = current_node.parent.parent

                else:
                    if current_node == current_node.parent.right:  # lr case
                        current_node = current_node.parent
                        self.rotate_left(current_node)

                    current_node.parent.color = self.B
                    current_node.parent.parent.color = self.R
                    self.rotate_right(current_node.parent.parent)

            else:
                uncle_node = current_node.parent.parent.left

                if uncle_node.color == self.R:  # uncle is red
                    current_node.parent.color = self.B
                    uncle_node.color = self.B
                    current_node.parent.parent.color = self.R
                    current_node = current_node.parent.parent

                else:
                    if current_node == current_node.parent.left:  # rl case
                        current_node = current_node.parent
                        self.rotate_right(current_node)

                    current_node.parent.color = self.B
                    current_node.parent.parent.color = self.R
                    self.rotate_left(current_node.parent.parent)

        # the root must be black
        self.root.color = self.B

    def search_recursive(self, current_node, key):
        # stop when NIL or the key is found
        if current_node == self.NIL or current_node.key == key:
            return current_node

        # search the left or right subtree
        if key < current_node.key:
            return self.search_recursive(current_node.left, key)
        else:
            return self.search_recursive(current_node.right, key)

    def delete(self, key):
        # find the node to delete
        delete_node = self.search_recursive(self.root, key)

        if delete_node == self.NIL:
            return

        replace_node = delete_node
        original_color = replace_node.color

        # delete a node with no left child
        if delete_node.left == self.NIL:
            child_node = delete_node.right
            self.transplant(delete_node, delete_node.right)

        # delete a node with no right child
        elif delete_node.right == self.NIL:
            child_node = delete_node.left
            self.transplant(delete_node, delete_node.left)

        # delete a node with two children
        else:
            # find the smallest node in the right subtree
            replace_node = self.find_min(delete_node.right)
            original_color = replace_node.color
            child_node = replace_node.right

            if replace_node.parent == delete_node:
                child_node.parent = replace_node
            else:
                self.transplant(replace_node, replace_node.right)
                replace_node.right = delete_node.right
                replace_node.right.parent = replace_node

            # move the replacement node
            self.transplant(delete_node, replace_node)
            replace_node.left = delete_node.left
            replace_node.left.parent = replace_node
            replace_node.color = delete_node.color

        # fix the color after deletion
        if original_color == self.B:
            self.delete_fixup(child_node)

        # reset the root and NIL node
        if self.root != self.NIL:
            self.root.parent = self.NIL

        self.NIL.color = self.B
        self.NIL.parent = self.NIL

    def transplant(self, old_node, new_node):
        # replace the old node with the new node
        if old_node.parent == self.NIL:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node

        new_node.parent = old_node.parent

    def delete_fixup(self, current_node):
        # fix the tree while the node is black
        while current_node != self.root and current_node.color == self.B:

            if current_node == current_node.parent.left:
                sibling_node = current_node.parent.right

                if sibling_node.color == self.R:  # sibling is red
                    sibling_node.color = self.B
                    current_node.parent.color = self.R
                    self.rotate_left(current_node.parent)
                    sibling_node = current_node.parent.right

                if sibling_node.left.color == self.B and sibling_node.right.color == self.B:
                    if sibling_node != self.NIL:
                        sibling_node.color = self.R
                    current_node = current_node.parent

                else:
                    if sibling_node.right.color == self.B:
                        sibling_node.left.color = self.B
                        sibling_node.color = self.R
                        self.rotate_right(sibling_node)
                        sibling_node = current_node.parent.right

                    sibling_node.color = current_node.parent.color
                    current_node.parent.color = self.B
                    sibling_node.right.color = self.B
                    self.rotate_left(current_node.parent)
                    current_node = self.root

            else:
                sibling_node = current_node.parent.left

                if sibling_node.color == self.R:  # sibling is red
                    sibling_node.color = self.B
                    current_node.parent.color = self.R
                    self.rotate_right(current_node.parent)
                    sibling_node = current_node.parent.left

                if sibling_node.right.color == self.B and sibling_node.left.color == self.B:
                    if sibling_node != self.NIL:
                        sibling_node.color = self.R
                    current_node = current_node.parent

                else:
                    if sibling_node.left.color == self.B:
                        sibling_node.right.color = self.B
                        sibling_node.color = self.R
                        self.rotate_left(sibling_node)
                        sibling_node = current_node.parent.left

                    sibling_node.color = current_node.parent.color
                    current_node.parent.color = self.B
                    sibling_node.left.color = self.B
                    self.rotate_right(current_node.parent)
                    current_node = self.root

        # make the current node black
        current_node.color = self.B

    def find_min(self, current_node):
        # find the smallest node
        while current_node.left != self.NIL:
            current_node = current_node.left
        return current_node

    def inorder(self):
        # print the nodes in sorted order
        self.inorder_recursive(self.root)
        print()

    def inorder_recursive(self, current_node):  # visit left, root, and right
        if current_node != self.NIL:
            self.inorder_recursive(current_node.left)

            # print the key and color
            print(str(current_node.key) + "(" + current_node.color + ")", end=' ')

            self.inorder_recursive(current_node.right)


if __name__ == "__main__":
    tree = RedBlackTree()

    for key in [50, 30, 70, 20, 40, 60, 80, 10]:
        tree.insert(key)

    tree.inorder()

    tree.delete(10)
    tree.inorder()

    tree.delete(30)
    tree.inorder()

    tree.delete(50)
    tree.inorder()