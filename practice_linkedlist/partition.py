# Write code to partition a linked list around a value x, 
# such that all nodes less than x come
# before all nodes greater than or equal to x.

def partition(self,pivot):

    a_head, a_tail = None, None
    b_head, b_tail = None, None
    node = self

    while node:
        if node.data < pivot:
            if a_head:
                a_tail.next, a_tail = node, node

            else:
                a_head, a_tail = node, node
        else:
            if b_head:
                b_tail.next, b_tail = node, node
            else:
                b_head, b_tail = node, node

        node = node.next

        a_tail.next = b_head
        return a_head
