# delete middle node from linked list.

def del_mid(self,n):
    current = self.head
    if current == n:
        return

    while current.next:
        if current.next == n:
            if current.next.next:
                current.next = current.next.next
            else:
                print("Cannot delete last node")
                return 
        current = current.next