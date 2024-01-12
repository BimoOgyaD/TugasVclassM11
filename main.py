from avl_tree import AVLTree

avl_tree = AVLTree()
avl_tree.insert_key(10)
avl_tree.insert_key(20)
avl_tree.insert_key(30)

# menampilkan AVL Tree structure
def print_avl_tree(node, depth=0):
    if node:
        print("  " * depth + f"- {node.key}")
        print_avl_tree(node.left, depth + 1)
        print_avl_tree(node.right, depth + 1)

print_avl_tree(avl_tree.root)
