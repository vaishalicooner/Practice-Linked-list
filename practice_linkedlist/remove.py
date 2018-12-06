# remove a node from linked list.
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __int__(self):
        self.head = None
        self.tail = None

    def remove_node(self,value):

        if self.head is not None and self.head.data == value:
            self.head - self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            else:
                current = current.next