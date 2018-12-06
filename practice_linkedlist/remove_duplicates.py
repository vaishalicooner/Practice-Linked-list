# remove duplicates from a linked list.

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __int__(self):
        self.head = None
        self.tail = None

    def remove_duplicates(self):

        node = self
        if node:
            values = {node.data = True}
            while node.next:
                if node.next.data in values:
                    node.next = node.next.next
                else:
                    values[node.next.data] = True
                    node = node.next
            return self
            