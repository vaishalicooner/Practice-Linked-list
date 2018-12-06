# append a node to linked list.

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def append_node(self,data):
    
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


class LinkedList(object):

    def __int__(self):
        self.head = None
        self.tail = None


