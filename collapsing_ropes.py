#python explorations 
import string

# I need the smallest list list of N letters and anti letters, where letters and anti letters annihilate eachother,
# such that it is stable against annihilation, until one letter/antiletter set is removed, upon which the string fully annihilates

# this means I need to traverse a list of letters and antiletters
### i will simply use integers with positive and negative, while traversing the linked list if a node and it's next node 
### sum to 0, annihilate both of them (set the previous node's next to current nodes next next)
# this means I need a way to represent letters and antiletters
### I will utilize a doubly linked list
# I need a function to check a string for annihilations
# once a single valid string is found, do not check any larger strings, but start small and work up with valid strings

class AnnihilationError(Exception):
    pass

class Node:
    def __init__(self, _value=None, _next=None, _prev=None):
        self.value = _value
        self.next = _next
        self.prev = _prev

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def check_destroy_next(self):
        if self.next is not None:
            return self.value + self.next.value == 0

class DLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def __repr__(self):
        return str(list(self))

    def __str__(self):
        return str(list(self))

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def link_node(self, before, after):
        before.next = after
        after.prev = before

    def add_node(self, node):
        if self.tail != self.head:
            self.link_node(self.tail, node)
        else:
            self.link_node(self.head, node)

        self.tail = node


    def annihilate_with_next(self, node):
        if node.next:
            if node.prev:
                self.link_node(node.prev, node.next.next)
            else:
                self.head = node.next.next
        else:
            raise AnnihilationError('Tried to annihilate end of list')



# make these into unit tests
dl = DLinkedList(Node(0))
dl.add_node(Node(1))
dl.add_node(Node(2))



# get letter translate dict
letters = string.ascii_lowercase

letters_translate = {}

for c in range(0, len(letters)):
    letters_translate[letters[c]] = c+1




