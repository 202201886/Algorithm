class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_to_array(root):
    if root is None:
        return []

    array = []
    queue = [(root, 0)]  # there are key, left, right in root

    while queue:  # while len(queue) > 0
        node, index = queue.pop(0)

        if index >= len(array):
            array.extend([None] * (index - len(array) + 1))

        array[index] = node.key

        if node.left:
            queue.append((node.left, 2 * index + 1))
        if node.right:
            queue.append((node.right, 2 * index + 2))

    return array

binary_tree_root = Node(10)
binary_tree_root.left = Node(20)
binary_tree_root.right = Node(30)
binary_tree_root.left.left = Node(40)
binary_tree_root.left.right = Node(50)

array_representation = tree_to_array(binary_tree_root)
print(array_representation)