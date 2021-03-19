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
        self.assertEqual(list(dl), [0, 1, 2])

    def test_annihilate(self):
        dl = DLinkedList(Node(0))
        for i in range(1, 5):
            dl.add_node(Node(i))

        e4 = dl.head.next.next
        dl.annihilate_with_next(e4)

        self.assertEqual(list(dl), [0, 1, 4])


if __name__ == '__main__':
    unittest.main()