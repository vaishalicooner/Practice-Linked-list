# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

def intersection(h1, h2):
    nodes = {}
    node = h1
    while node:
        nodes[node] = True
        node = node.next

    node = h2
    while node:
        if node in nodes:
            return node

        node = node.next
    return node
    
