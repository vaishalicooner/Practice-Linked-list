# print each nodes data in a linked list.

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __int__(self):
        self.head = None
        self.tail = None


    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next