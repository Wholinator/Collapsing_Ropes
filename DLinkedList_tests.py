import unittest

from collapsing_ropes import DLinkedList, Node

class TestLinkedList(unittest.TestCase):
    def test_create(self):
        dl = DLinkedList(Node(0))
        self.assertEqual(dl.head.value, 0)
        self.assertEqual(dl.tail.value, 0)

    def test_add(self):
        dl = DLinkedList(Node(0))
        dl.add_node(Node(1))
        self.assertEqual(dl.head.value, 0)
        self.assertEqual(dl.tail.value, 1)

        dl.add_node(Node(2))
        self.assertEqual(dl.value_list(), [0, 1, 2])

    def test_annihilate(self):
        dl = DLinkedList(Node(0))
        for i in range(1, 5):
            dl.add_node(Node(i))

        e4 = dl.head.next.next
        dl.annihilate_with_next(e4)

        self.assertEqual(dl.value_list(), [0, 1, 4])

    def test_remove_all_of_value(self):
        dl = DLinkedList()
        for i in list(range(-9, 10))*2:
            dl.add_node(Node(i))

        dl.remove_all_of_value(5)
        self.assertFalse(5 in dl.value_list())

        for i in [9, 8, 10, -3, 0]:
            dl.remove_all_of_value(i)
        self.assertFalse(8 in dl.value_list() or 9 in dl.value_list())

        for i in [1, 2, 4]:
            dl.remove_all_of_value(i)
        
        self.assertEqual(dl.value_list(), [-7, -6, 6, 7, -7, -6, 6, 7])
        


if __name__ == '__main__':
    unittest.main()