# searching a given a node in linked list

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __int__(self):
        self.head = None
        self.tail = None

    def find(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True

            current = current.next
        return False