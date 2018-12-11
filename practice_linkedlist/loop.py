# Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

def loop(self):
    nodes = {}
    node = self
    while node:
        if node in nodes:
            return node
        nodes[node] = True
        node = node.next
        
    return None