import unittest
from avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_insert(self):
        avl_tree = AVLTree()
        avl_tree.insert_key(10)
        avl_tree.insert_key(20)
        avl_tree.insert_key(30)

        #bisa ditambahkan jika kita mau. tetapi sebagai referensi implementasi saya hanya mengetikkanya sampai sini
